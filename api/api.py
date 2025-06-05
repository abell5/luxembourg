import os
import json

# import pickle
from dotenv import dotenv_values
import pandas as pd
import torch
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from . import (
    load_model,
    generate_output_stream,
    edit_output,
    parse_connected_json_objects,
)

# from .safenudge import SafeNudge
from transformers import AutoTokenizer, AutoModelForCausalLM
from .wildguard_safenudge import WildGuard, WildGuardSafeNudge

CUDA = torch.cuda.is_available()
MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"

if "HF_TOKEN" in os.environ:
    TOKEN = os.environ["HF_TOKEN"]
else:
    TOKEN = dotenv_values()["HF_TOKEN"]

ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Wildguard
    ml_models["SAFENUDGE_TOKENIZER"] = AutoTokenizer.from_pretrained(
        "allenai/wildguard", token=TOKEN
    )
    ml_models["SAFENUDGE_CLF"] = AutoModelForCausalLM.from_pretrained(
        "allenai/wildguard", token=TOKEN
    )
    if CUDA:
        ml_models["SAFENUDGE_CLF"].to("cuda")

    ml_models["WILDGUARD"] = WildGuard(
        model=ml_models["SAFENUDGE_CLF"], tokenizer=ml_models["SAFENUDGE_TOKENIZER"]
    )

    # LLM
    ml_models["model"], ml_models["tokenizer"] = load_model(
        MODEL_NAME, token=TOKEN, cuda=CUDA
    )
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",  # This could be a security risk...
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["X-Requested-With", "Content-Type"],
)


@app.get("/")
async def root():
    # TODO: Return info on available endpoints with description of parameters
    return {"message": "Hello World"}


@app.post("/generate", summary="Generate an output")
async def generate(
    init_prompt: str,
    k: int = 30,
    T: float = 1,
    tau: float = 0.5,
    max_new_tokens: int = 100,
    sleep_time: float = 0.0,
    verbose: bool = False,
    random_state: int = None,
    data: list = None,
    safenudge: bool = False,
):
    """
    Generate an output stream based on a prompt, using a LLM (Llama 3.2 1B Instruct).
    """
    print(safenudge)
    if not safenudge:
        data = generate_output_stream(
            init_prompt=init_prompt,
            model=ml_models["model"],
            tokenizer=ml_models["tokenizer"],
            k=k,
            T=T,
            max_new_tokens=max_new_tokens,
            sleep_time=sleep_time,
            cuda=CUDA,
            verbose=verbose,
            random_state=random_state,
            data=data,
        )
        return StreamingResponse(data, media_type="application/json")
    else:
        data = WildGuardSafeNudge(
            model=ml_models["model"],
            tokenizer=ml_models["tokenizer"],
            mode="topk",
            k=k,
            temperature=T,
            random_state=random_state,
            cuda=CUDA,
        ).generate_moderated(
            prompt=init_prompt,
            # clf=SAFENUDGE_CLF,
            clf=ml_models["WILDGUARD"],
            target="",
            tau=tau,
            max_tokens=max_new_tokens,
            verbose=verbose,
        )
        return StreamingResponse(data, media_type="application/json")


def edit(
    data: list,
    token_pos: int,
    new_token: int,
):
    """
    Edit an output based on a token position and a new token and returns the edited
    output, truncated to the token position.
    """
    data = pd.DataFrame(json.loads(data))
    data = edit_output(data, token_pos, new_token)
    return data


@app.post("/regenerate", summary="Generate an output")
async def regenerate(
    init_prompt: str,
    k: int = 30,
    T: float = 1,
    max_new_tokens: int = 100,
    sleep_time: float = 0.0,
    verbose: bool = False,
    random_state: int = None,
    content: str = None,
    token_pos: int = None,
    new_token: str = None,
):
    """
    Generate an output stream based on a prompt, using a LLM (Llama 3.2 1B Instruct).
    """
    if (content is not None) and (token_pos is not None) and (new_token is not None):
        content = parse_connected_json_objects(content)
        new_token_idx = content[token_pos]["texts"].index(new_token)
        content = json.dumps(content)
        data = edit(content, token_pos, new_token_idx)

    result = generate_output_stream(
        init_prompt=init_prompt,
        model=ml_models["model"],
        tokenizer=ml_models["tokenizer"],
        k=k,
        T=T,
        max_new_tokens=max_new_tokens,
        sleep_time=sleep_time,
        cuda=CUDA,
        verbose=verbose,
        random_state=random_state,
        data=data,
    )
    return StreamingResponse(result, media_type="application/json")
