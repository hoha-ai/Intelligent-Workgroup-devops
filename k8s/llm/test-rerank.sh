curl -X POST "http://localhost:9089/score" \
	-H "Content-Type: application/json" \
	-d '{
  "model": "bge-reranker-v2-m3",
  "text_1": "华南理工大学怎么样",
  "text_2": [
    "华南师范大学怎么样",
    "华南理工大学师资好"
  ]
}'

# /home/root123/anaconda3/envs/DeepSeekR1/bin/python /home/root123/anaconda3/envs/DeepSeekR1/bin/vllm serve /home/root123/bge-reranker-v2-m3 --served-model-name bge-reranker-v2-m3 --tensor-parallel-size 2 --enforce-eager --gpu_memory_utilization=0.1 --enable-chunked-prefill=False --host 0.0.0.0 --port 9089
