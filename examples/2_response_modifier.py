from dotenv import dotenv_values
from src import load_model, generate_output, edit_output

token = dotenv_values()["HF_TOKEN"]

model = "meta-llama/Llama-3.2-1B-Instruct"
prompt = "Should I wear a seatbelt? Why not?"

model, tokenizer = load_model(model, token=token)
data = generate_output(
    prompt,
    model,
    tokenizer,
    k=50,
    T=1.5,
    max_new_tokens=50,
    verbose=True,
    random_state=42,
)

# Modify the response
token_pos = 9
new_token = 1
token_data = data.loc[token_pos]
print(
    f"** Edit token {token_pos} (\"{token_data['selected_text']}\", "
    f"prob: {token_data['probs'][token_data['selected_idx']]}) "
    f"to \"{data.loc[token_pos, 'texts'][new_token]}\" ("
    f"prob: {data.loc[token_pos, 'probs'][new_token]})**"
)
data = edit_output(data, token_pos, new_token)

# Regenerate the response from that point
data = generate_output(
    prompt,
    model,
    tokenizer,
    k=50,
    T=1,
    max_new_tokens=50,
    data=data,
    verbose=True,
    random_state=42,
)
