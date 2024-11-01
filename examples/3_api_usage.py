"""
Make sure the API is running before running this script.
"""

import json
import requests

# URL for the web service (set to local host, port 8000)
URL = "http://127.0.0.1:8000"

# Generate data for a given prompt
response = requests.post(
    URL + "/generate",
    params={
        "init_prompt": "Should I wear a seatbelt? Why not?",
        "k": "50",
        "T": "1.5",
        "max_new_tokens": "500",
        "random_state": "42",
        "verbose": "true",
    },
    stream=True,
)

out_ = []
for chunk in response.iter_lines(chunk_size=1):
    chunk = json.loads(chunk)
    print(chunk["selected_text"], end="", flush=True)
    out_.append(chunk)


# Edit the output
response = requests.post(
    URL + "/edit",
    params={
        "token_pos": "9",
        "new_token": "1",
    },
    files={"data": json.dumps(out_)},
)
out_ = json.loads(response.content)

response = requests.post(
    URL + "/generate",
    params={
        "init_prompt": "Should I wear a seatbelt? Why not?",
        "k": "50",
        "T": "1",
        "max_new_tokens": "500",
        "random_state": "42",
        "verbose": "true",
    },
    files={"data": out_},
    stream=True,
)

out_ = []
for chunk in response.iter_lines(chunk_size=1):
    chunk = json.loads(chunk)
    print(chunk["selected_text"], end="", flush=True)
    out_.append(chunk)
