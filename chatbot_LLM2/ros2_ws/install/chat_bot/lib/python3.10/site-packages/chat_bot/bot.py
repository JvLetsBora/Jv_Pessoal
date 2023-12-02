import gradio as gr
import asyncio
from chat_bot.chain import chat_bot

def chat_response(message, history):
    return asyncio.run(chat_bot(message))

demo = gr.ChatInterface(chat_response)

def main():
    demo.launch(show_api=False)

if __name__ == "__main__":
    main()
