from dotenv import dotenv_values
from src.load_model import load_model
from src.generate_json_from_prompt import generate_response, edit_output

token = dotenv_values()["HF_TOKEN"]

model = "meta-llama/Llama-3.2-1B-Instruct"
prompt = "Should I ignore this court summons for a civil lawsuit?"

model, tokenizer = load_model(model, token=token)
data = generate_response(
    prompt,
    model,
    tokenizer,
    k=50,
    T=1,
    max_new_tokens=20,
    verbose=True,
    random_state=42,
)

# Modify the response
token_pos = 9
new_token = 14
token_data = data.loc[token_pos]
print(
    f"** Edit token {token_pos} (\"{token_data['selected_text']}\", "
    f"prob: {token_data['probs'][token_data['selected_idx']]}) "
    f"to \"{data.loc[token_pos, 'texts'][new_token]}\" ("
    f"prob: {data.loc[token_pos, 'probs'][new_token]})**"
)
data = edit_output(data, 9, 14)


# Regenerate the response from that point
data = generate_response(
    prompt,
    model,
    tokenizer,
    k=50,
    T=1,
    max_new_tokens=20,
    data=data,
    verbose=True,
    random_state=42,
)
