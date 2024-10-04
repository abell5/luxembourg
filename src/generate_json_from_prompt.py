import pandas as pd
import numpy as np
import torch

def generate_response(
    model,
    tokenizer,
    init_prompt,
    k = 10,
    T = 0.5,
    max_new_tokens = 100,
    verbose=True
):
    
    TERMINATOR = tokenizer.eos_token

    new_tokens = []

    data = pd.DataFrame(columns=['texts','probs','selected_idx'])
    
    prompt = init_prompt
    while not(prompt.find(TERMINATOR) >= 0 or len(new_tokens) >= max_new_tokens):
        prompt = init_prompt + ''.join(new_tokens)

        if verbose:
            print(prompt)
        
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        input_ids = input_ids.cuda()
        
        with torch.no_grad():
            outputs = model(input_ids, use_cache=False, output_hidden_states=True, output_attentions=False)
            logits = outputs['logits']
        
        input_ids = input_ids.cpu()
        logits = logits.cpu()
        logits = logits[-1, -1]
        
        logits_topk, logits_topk_idx = torch.topk(logits, k)
        
        texts_topk = tokenizer.convert_ids_to_tokens(logits_topk_idx)
        probs_topk = torch.nn.functional.softmax(logits_topk/T, dim=-1)
        probs_topk = probs_topk.detach().numpy()
        
        next_idx = np.random.choice(len(texts_topk),p=probs_topk)
    
        new_tokens.append(texts_topk[next_idx])    
    
        d = {'texts': texts_topk,
             'probs': probs_topk,
             'selected_idx': next_idx}
        
        data.loc[len(data)] = d

    return data

#if __name__ == '__main__':