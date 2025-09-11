curl http://localhost:8088/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "qwen-2.5-vl",
    "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": "'$1'"}},
        {"type": "text", "text": "'$2'"}
    ]}
    ]
    }'
