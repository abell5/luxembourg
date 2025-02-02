import pickle
import json
from time import sleep
import pandas as pd
import numpy as np
import torch


def generate_output_stream(
    init_prompt,
    generated_output,
    model,
    tokenizer,
    k=10,
    T=0.5,
    max_new_tokens=100,
    sleep_time=0,
    data=None,
    cuda=False,
    verbose=True,
    random_state=None,
    as_json=True,
):
    rng = np.random.default_rng(random_state)
    TERMINATOR = tokenizer.eos_token
    idx_counter = 0

    for d in generated_output:
        if as_json:
            d = json.dumps(d) + "\n"
        yield d
        idx_counter += 1

    if data is None:
        data = pd.DataFrame(
            columns=[
                "idx_counter",
                "texts",
                "token_ids",
                "probs",
                "selected_idx",
                "selected_text",
            ]
        )

        output = ""
        output_ids = torch.tensor([], dtype=torch.long)
    else:
        output = data["selected_text"].str.cat(sep="")
        output_ids = torch.tensor(
            data.apply(
                lambda row: row["token_ids"][row["selected_idx"]], axis=1
            ).tolist()
        ).reshape(1, -1)

    if verbose:
        print(init_prompt)
        print(output, end="", flush=True)

    prompt = [
        {"role": "user", "content": init_prompt},
        {"role": "assistant", "content": ""},
    ]
    prompt_ids = tokenizer.apply_chat_template(prompt, return_tensors="pt")[0][
        :-1
    ].reshape(1, -1)

    while not (output.find(TERMINATOR) >= 0 or output_ids.shape[-1] >= max_new_tokens):

        if cuda:
            prompt_ids = prompt_ids.cuda()
            output_ids = output_ids.cuda()

        with torch.no_grad():
            all_ids = torch.cat([prompt_ids, output_ids], dim=-1)
            outputs = model(
                all_ids,
                use_cache=False,
                output_hidden_states=True,
                output_attentions=False,
            )
            logits = outputs["logits"]

        # prompt_ids = prompt_ids.cpu()
        logits = logits.cpu()
        logits = logits[-1, -1]

        logits_topk, logits_topk_idx = torch.topk(logits, k)

        texts_topk = [tokenizer.decode(idx) for idx in logits_topk_idx]
        probs_topk = torch.nn.functional.softmax(logits_topk / T, dim=-1)
        probs_topk = probs_topk.detach().numpy()

        next_idx = rng.choice(len(texts_topk), p=probs_topk)

        d = {
            "idx_counter": idx_counter,
            "texts": texts_topk,
            "token_ids": logits_topk_idx.tolist(),
            "probs": probs_topk.tolist(),
            "selected_idx": next_idx,
            "selected_text": texts_topk[next_idx],
        }
        idx_counter += 1

        data.loc[len(data)] = d

        output += texts_topk[next_idx]
        output_ids = torch.cat(
            [output_ids.cpu(), logits_topk_idx[next_idx].reshape(1, -1)], dim=-1
        )

        if verbose:
            print(texts_topk[next_idx], end="", flush=True)

        generated_output.append(d)

        if as_json:
            d = json.dumps(d) + "\n"

        yield d
        sleep(sleep_time)

    pickle.dump(generated_output, open('generated_output.pkl', 'wb'))

    if cuda:
        del prompt_ids

    if verbose:
        print()


def generate_output(
    init_prompt,
    model,
    tokenizer,
    k=10,
    T=0.5,
    max_new_tokens=100,
    data=None,
    cuda=False,
    verbose=True,
    random_state=None,
):
    data = generate_output_stream(
        init_prompt,
        model,
        tokenizer,
        k=k,
        T=T,
        max_new_tokens=max_new_tokens,
        data=data,
        cuda=cuda,
        verbose=verbose,
        random_state=random_state,
        as_json=False,
    )
    return pd.DataFrame(data)


# def edit_output(data: list, token_pos: int, new_token: int) -> pd.DataFrame:
#     data = pd.DataFrame(data)
#     new_text = data.loc[token_pos, "texts"][new_token]
#     data.loc[token_pos, "selected_idx"] = new_token
#     data.loc[token_pos, "selected_text"] = new_text
#
#     # Drop all entries after the modified token
#     data.drop(range(token_pos + 1, len(data)), inplace=True)
#     return data


def edit_output(
    data: list, token_pos: int, new_token_str: str, tokenizer
) -> pd.DataFrame:
    data = pd.DataFrame(data)

    # Get ids of new text
    new_token_ids = tokenizer.encode(new_token_str)[1:]
    new_token_strs = [tokenizer.decode(x) for x in new_token_ids]

    # The loop is applied just in case the tokenizer breaks a token string into 2 ids
    # (probably won't ever happen, but just to be sure...)
    for offset, (token_id, token_str) in enumerate(zip(new_token_ids, new_token_strs)):

        if token_str not in data.loc[token_pos + offset, "texts"]:
            data.loc[token_pos + offset, "texts"].insert(0, token_str)
            data.loc[token_pos + offset, "token_ids"].insert(0, token_id)
            data.loc[token_pos + offset, "probs"].insert(0, 1.0)

        token_idx = data.loc[token_pos + offset, "texts"].index(token_str)
        data.loc[token_pos + offset, "selected_idx"] = token_idx
        data.loc[token_pos + offset, "selected_text"] = token_str

    data["idx_counter"] = list(range(data.shape[0]))

    # Drop all entries after the modified token
    data.drop(range(token_pos + offset + 1, len(data)), inplace=True)
    return data


# def regenerate_output(
#     generated_output: list,
#     idx_counter: int,
#     new_token_str: str,
#     init_prompt,
#     model,
#     tokenizer,
#     k=10,
#     T=0.5,
#     max_new_tokens=100,
#     sleep_time=0,
#     cuda=False,
#     verbose=True,
#     random_state=None,
#     as_json=True,
# ):
#     """
#     input_prompt contains token ids
#     generated_output contains the results generation data
#     idx_counter is the index within generated_output to modify
#     new_token_str is the new token to insert in-place
#     """
#     data = edit_output(generated_output, idx_counter, new_token_str, tokenizer)
#     generated_output = data.to_json(orient="records")
#
#     data = generate_output_stream(
#         init_prompt=init_prompt,
#         generated_output=data,
#         model=model,
#         tokenizer=tokenizer,
#         k=k,
#         T=T,
#         max_new_tokens=max_new_tokens,
#         sleep_time=sleep_time,
#         data=data,
#         cuda=cuda,
#         verbose=verbose,
#         random_state=random_state,
#         as_json=as_json,
#     )
