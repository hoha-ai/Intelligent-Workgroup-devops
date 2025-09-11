from transformers import AutoModel, AutoTokenizer
from fastapi import FastAPI, Request, HTTPException
import torch
from typing import List

app = FastAPI()

# Load model and tokenizer
model_name = "/opt/bce-embedding-base_v1/"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

@app.post("/v1/embeddings")
async def embed(request: Request):
    # Parse the request body
    try:
        data = await request.json()
        inputs = data["input"]  # List of texts
        model_name = data["model"]  # Model name (unused in this example)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid request: {str(e)}")

    # Tokenize and generate embeddings
    try:
        encoded_inputs = tokenizer(inputs, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = model(**encoded_inputs)
        # Mean pooling to get sentence embeddings
        embeddings = outputs.last_hidden_state.mean(dim=1).tolist()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding generation failed: {str(e)}")

    # Format the response in OpenAI-style
    response_data = [{"embedding": emb} for emb in embeddings]
    return {"data": response_data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9088)
