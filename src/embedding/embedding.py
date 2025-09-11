from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from sentence_transformers import SentenceTransformer

app = FastAPI()

# 加载嵌入模型
model = SentenceTransformer(rf"/app/bce-embedding-base_v1")

class EmbeddingRequest(BaseModel):
    texts: List[str]  # 支持多条文本

@app.post("/embed")
async def embed(request: EmbeddingRequest):
    # 批量生成嵌入向量
    embeddings = model.encode(request.texts)
    return {"embeddings": embeddings.tolist()}  # 返回多条文本的嵌入向量

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8088)

