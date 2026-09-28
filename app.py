import streamlit as st

# st.title("hello)")
# name=st.text_input("jose")
# st.write(f"hi,{name}!")

# st.title("Mini Chatbot")
# prompt=st.chat_input("Say something!")

# if prompt:
#     with st.chat_message("User:"):
#         st.write(prompt)

#     with st.chat_message("Avatar:"):
#         st.write(f"you said: {prompt}")    


# if "count" not in st.session_state:
#     st.session_state.count =0

# if st.button("Add"):
#     st.session_state.count+= 1

# st.write(st.session_state.count)

# import streamlit as st

# st.title("Mini bot with memory")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.write(msg["content"])

# prompt = st.chat_input("Say something")

# if prompt:
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.write(prompt)

#     reply = f"You said: {prompt}"
#     st.session_state.messages.append({"role": "assistant", "content": reply})
#     with st.chat_message("assistant"):
#         st.write(reply)

# import streamlit as st
# from huggingface_hub import InferenceClient

# st.title("Mini Chatbot")

# client = InferenceClient(model="meta-llama/Llama-3.1-8B-Instruct")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.write(msg["content"])

# prompt = st.chat_input("Ask me something")

# if prompt:
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.write(prompt)

#     response = client.chat_completion(
#         messages=st.session_state.messages,
#         max_tokens=1300,
#     )
#     reply = response.choices[0].message.content

#     st.session_state.messages.append({"role": "assistant", "content": reply})
#     with st.chat_message("assistant"):
#         st.write(reply)

#With streaming :
# import streamlit as st
# from huggingface_hub import InferenceClient

# st.title("Mini Chatbot")

# client = InferenceClient(model="meta-llama/Llama-3.1-8B-Instruct")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.write(msg["content"])

# def get_reply():
#     stream = client.chat_completion(
#         messages=st.session_state.messages,
#         max_tokens=1000,
#         stream=True,
#     )
#     for chunk in stream:
#         if not chunk.choices:
#             continue
#         text = chunk.choices[0].delta.content
#         if text:
#             yield text

# prompt = st.chat_input("Ask me something")

# if prompt:
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.write(prompt)

#     with st.chat_message("assistant"):
#         reply = st.write_stream(get_reply())

#     st.session_state.messages.append({"role": "assistant", "content": reply})


#Added avatar :
import streamlit as st
from huggingface_hub import InferenceClient

st.title("Mini Chatbot")

client = InferenceClient(model="meta-llama/Llama-3.1-8B-Instruct")

AVATARS = {"user": "🧑‍💻", "assistant": "🤖"}

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=AVATARS[msg["role"]]):
        st.write(msg["content"])

def get_reply():
    stream = client.chat_completion(
        messages=st.session_state.messages,
        max_tokens=1000,
        stream=True,
    )
    for chunk in stream:
        if not chunk.choices:
            continue
        text = chunk.choices[0].delta.content
        if text:
            yield text

prompt = st.chat_input("Ask me something")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=AVATARS["user"]):
        st.write(prompt)

    with st.chat_message("assistant", avatar=AVATARS["assistant"]):
        reply = st.write_stream(get_reply())

    st.session_state.messages.append({"role": "assistant", "content": reply})



