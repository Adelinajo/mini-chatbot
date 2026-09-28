# 1.Creating a simple text msg 
# import chainlit as cl

# @cl.on_message
# async def main(message: cl.Message):
#     await cl.Message(content=f"You said: {message.content}").send()


    #2.checking session_state in chainlit
# import chainlit as cl

# @cl.on_chat_start
# async def start():
#     cl.user_session.set("history", [])

# @cl.on_message
# async def main(message: cl.Message):
#     history = cl.user_session.get("history")
#     history.append({"role": "user", "content": message.content})

#     reply = f"You have sent {len(history)} message(s) so far."
#     await cl.Message(content=reply).send()

#3.checking with hugging face model:

# import chainlit as cl
# from huggingface_hub import AsyncInferenceClient

# client = AsyncInferenceClient(model="meta-llama/Llama-3.1-8B-Instruct")

# @cl.on_chat_start
# async def start():
#     cl.user_session.set("history", [])

# @cl.on_message
# async def main(message: cl.Message):
#     history = cl.user_session.get("history")
#     history.append({"role": "user", "content": message.content})

#     response = await client.chat_completion(
#         messages=history,
#         max_tokens=1000,
#     )
#     reply = response.choices[0].message.content

#     history.append({"role": "assistant", "content": reply})
#     await cl.Message(content=reply).send()

#4.Adding streaming in chainlit
import chainlit as cl
from huggingface_hub import AsyncInferenceClient

client = AsyncInferenceClient(model="meta-llama/Llama-3.1-8B-Instruct")

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])

@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")

    stream = await client.chat_completion(
        messages=history,
        max_tokens=1000,
        stream=True,
    )

    async for chunk in stream:
        if not chunk.choices:
            continue
        text = chunk.choices[0].delta.content
        if text:
            await msg.stream_token(text)

    history.append({"role": "assistant", "content": msg.content})
    await msg.send()
