# luxembourg

https://www.eurovis2025.lu/

## Installation
To run the project, make sure you have `podman` installed on your system. If
you don't have it installed, you can install it by following the instructions
on the [official website](https://podman.io/getting-started/installation).

You will also need an access token for Hugging Face. You can get one by
creating an account on the [Hugging Face website](https://huggingface.co/).
Afer creating an account, you can get your access token by visiting the
[Hugging Face API page](https://huggingface.co/settings/tokens).
Next, modify the `.env` file in the project directory and replace
`YOUR_HUGGINGFACE_TOKEN` value with your access token. Finally, you will need
to request access permission for the `Llama-3.1-8B-Instruct` model by visiting
the [model's Hugging Face page](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).

```bash
# Clone the repository
git clone https://github.com/abell5/luxembourg.git

# Change to the project directory
cd luxembourg

# Build and run the container
make run
```
