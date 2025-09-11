
prompt='{"messages":[{"content":"/nothink","role":"system"},{"content":"问题: 中国首都是哪里\n**只回答结论**\n**如果你接收到的问题存在影响回答质量的干扰因素，请提示用户。情况严重时可不必强行输出答案。**","role":"user"}],"model":"qwen-2.5","stream":false, "chat_template_kwargs": {"enable_thinking": false}}'

echo $prompt > /tmp/a.txt

curl -X POST "http://localhost:8088/v1/chat/completions" \
     -H "Content-Type: application/json" \
     -d@/tmp/a.txt

# /home/zdzn/anaconda3/envs/DeepSeekR1/bin/python /home/zdzn/anaconda3/envs/DeepSeekR1/bin/vllm serve /home/zdzn/Qwen2.5-32B-Instruct-GPTQ-Int4/ --served-model-name qwen-2.5 --tensor-parallel-size 2 --max-model-len 10000 --enforce-eager --gpu_memory_utilization=0.8 --enable-chunked-prefill=False --host 0.0.0.0 --port 8088
