curl -X POST "http://localhost:9088/tokenize" \
	-H "Content-Type: application/json" \
	-d '{
    "model": "bce-embedding-base_v1",
    "prompt": "This is a cat."
}'

# /home/zdzn/anaconda3/envs/DeepSeekR1/bin/python /home/zdzn/anaconda3/envs/DeepSeekR1/bin/vllm serve /home/zdzn/bce-embedding-base_v1/ --served-model-name bce-embedding-base_v1 --tensor-parallel-size 2 --enforce-eager --gpu_memory_utilization=0.2 --enable-chunked-prefill=False --host 0.0.0.0 --port 9088
