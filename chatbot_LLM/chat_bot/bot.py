import gradio as gr
from  chain import chat_bot


def chat_response(message, history):
    return chat_bot(message)

demo = gr.ChatInterface(chat_response)


if __name__ == "__main__":
    demo.launch()