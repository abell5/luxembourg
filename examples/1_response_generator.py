from dotenv import dotenv_values
from api import load_model, generate_output

token = dotenv_values()["HF_TOKEN"]

model = "meta-llama/Llama-3.2-1B-Instruct"

model, tokenizer = load_model(model, token=token)
data = generate_output(
    "Should I wear a seatbelt?",
    model,
    tokenizer,
    k=10,
    T=0.2,
    max_new_tokens=20,
    verbose=True,
)
