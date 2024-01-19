import openai
import gradio as gr

openai.api_key = "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" #this api is disabled

messages = [{"role": "system", "content": "You are a psycologist"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Your Title")

demo.launch(share=True)
