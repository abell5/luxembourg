import os
import pickle
# from copy import deepcopy
import json
from dotenv import dotenv_values
import pandas as pd
import torch
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from . import (
    load_model,
    generate_output,
    generate_output_stream,
    edit_output,
)

CUDA = torch.cuda.is_available()
MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"

# Super scrapy patching for the demo
# generated_output = []
pickle.dump([], open('generated_output.pkl', 'wb'))
# input_prompt = ""
pickle.dump("", open('input_prompt.pkl', 'wb'))

if "HF_TOKEN" in os.environ:
    TOKEN = os.environ["HF_TOKEN"]
else:
    TOKEN = dotenv_values()["HF_TOKEN"]

model, tokenizer = load_model(MODEL_NAME, token=TOKEN, cuda=CUDA)

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
    generated_output = []
    pickle.dump(generated_output, open('generated_output.pkl', 'wb'))
    pickle.dump(init_prompt, open('input_prompt.pkl', 'wb'))
    # print(input_prompt)
    # print(generated_output)

    if data is not None:
        data = pd.DataFrame(json.loads(data[0]))

    data = generate_output_stream(
        init_prompt=init_prompt,
        generated_output=generated_output,
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
    return data


@app.post("/regenerate", summary="Generate the output while editing a specific token.")
async def regenerate(
    # generated_output: list,
    idx_counter: int,
    new_token_str: str,
    # model,
    # tokenizer,
    k: int = 30,
    T: float = 1,
    max_new_tokens: int = 100,
    sleep_time: float = 0.0,
    verbose: bool = False,
    random_state: int = None,
):
    input_prompt = pickle.load(open('input_prompt.pkl', 'rb'))
    generated_output = pickle.load(open('generated_output.pkl', 'rb'))
    print(input_prompt)

    data = edit_output(generated_output, idx_counter, new_token_str, tokenizer)
    generated_output = json.loads(data.to_json(orient="records"))

    data = generate_output_stream(
        init_prompt=input_prompt,
        generated_output=generated_output,
        model=model,
        tokenizer=tokenizer,
        k=k,
        T=T,
        max_new_tokens=max_new_tokens,
        sleep_time=sleep_time,
        data=data,
        cuda=CUDA,
        verbose=verbose,
        random_state=random_state,
        as_json=True,
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
    data = edit_output(data, token_pos, new_token)
    return data.to_json(orient="records")
