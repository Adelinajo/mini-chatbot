# from huggingface_hub import InferenceClient

# client = InferenceClient(model="meta-llama/Llama-3.1-8B-Instruct")

# messages = [
#     {"role": "user", "content": "What is Streamlit in one sentence?"}
# ]

# response = client.chat_completion(messages=messages, max_tokens=200)
# print(response.choices[0].message.content)

from huggingface_hub import InferenceClient

client = InferenceClient(model="meta-llama/Llama-3.1-8B-Instruct")

messages = [
    {"role": "user", "content": "Give me 3 tips for learning Python."}
]

stream = client.chat_completion(messages=messages, max_tokens=500, stream=True)

for chunk in stream:
    if not chunk.choices:
        continue
    text = chunk.choices[0].delta.content
    if text:
        print(text, end="", flush=True)