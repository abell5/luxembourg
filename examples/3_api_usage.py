"""
Make sure the API is running before running this script.
"""

import json
import requests

# URL for the web service (set to local host, port 8000)
URL = "http://127.0.0.1:8000"
# URL = "https://llm-viz.users.hsrn.nyu.edu"

# Generate data for a given prompt
response = requests.post(
    URL + "/generate",
    params={
        "init_prompt": "Should I wear a seatbelt? Why not?",
        "k": "100",
        "T": "1",
        "max_new_tokens": "12",
        "random_state": "0",
        "verbose": "false",
    },
    stream=True,
)

out_ = []
for chunk in response.iter_lines(chunk_size=1):
    chunk = json.loads(chunk)
    print(chunk["selected_text"], end="", flush=True)
    out_.append(chunk)
print()

# Edit the output
# response = requests.post(
#     URL + "/edit",
#     params={
#         "token_pos": "7",
#         "new_token": "34",
#     },
#     files={"data": json.dumps(out_)},
# )
# out_ = json.loads(response.content)

response = requests.post(
    URL + "/regenerate",
    params={
        "init_prompt": "Should I wear a seatbelt? Why not?",
        "k": "50",
        "T": "1.5",
        "max_new_tokens": "500",
        "random_state": "42",
        "verbose": "false",
        "token_pos": "5",
        "new_token": "6",
        "content": json.dumps(out_),
    },
    stream=True,
)

print("".join([s["selected_text"] for s in out_[:5]]), end="", flush=True)
out_ = []
for chunk in response.iter_lines(chunk_size=1):
    chunk = json.loads(chunk)
    print(chunk["selected_text"], end="", flush=True)
    out_.append(chunk)
