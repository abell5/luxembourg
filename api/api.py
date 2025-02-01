import os
import json
from dotenv import dotenv_values
import pandas as pd
import torch
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from . import load_model, generate_output, generate_output_stream, edit_output

CUDA = torch.cuda.is_available()
MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"

if "HF_TOKEN" in os.environ:
    TOKEN = os.environ["HF_TOKEN"]
else:
    TOKEN = dotenv_values()["HF_TOKEN"]

model, tokenizer = load_model(MODEL_NAME, token=TOKEN, cuda=True)

app = FastAPI()

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
    max_new_tokens: int = 100,
    sleep_time: float = 0.0,
    verbose: bool = False,
    random_state: int = None,
    data: list = None,
):
    """
    Generate an output stream based on a prompt, using a LLM (Llama 3.2 1B Instruct).
    """
    if data is not None:
        print(json.loads(data[0]))
        data = pd.DataFrame(json.loads(data[0]))

    data = generate_output_stream(
        init_prompt=init_prompt,
        model=model,
        tokenizer=tokenizer,
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


@app.post("/generate_static", summary="Generate an output")
async def generate_static(
    init_prompt: str,
    k: int = 30,
    T: float = 1,
    max_new_tokens: int = 100,
    verbose: bool = False,
    random_state: int = None,
    data: list = None,
):
    """
    Generate an output stream based on a prompt, using a LLM (Llama 3.2 1B Instruct).
    """
    if data is not None:
        print(json.loads(data[0]))
        data = pd.DataFrame(json.loads(data[0]))

    data = generate_output(
        init_prompt=init_prompt,
        model=model,
        tokenizer=tokenizer,
        k=k,
        T=T,
        max_new_tokens=max_new_tokens,
        cuda=CUDA,
        verbose=verbose,
        random_state=random_state,
        data=data,
    )
    return StreamingResponse(data, media_type="application/json")


@app.post("/edit", summary="Edit an output")
async def edit(
    data: list,
    token_pos: int,
    new_token: int,
):
    """
    Edit an output based on a token position and a new token and returns the edited
    output, truncated to the token position.
    """
    data = pd.DataFrame(json.loads(data[0]))
    print(data)
    data = edit_output(data, token_pos, new_token)
    return data.to_json(orient="records")
