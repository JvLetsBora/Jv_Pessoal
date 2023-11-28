import gradio as gr
from  chat_bot.chain import chat_bot
import subprocess
import threading
import time



def chat_response(message, history):
    return chat_bot(message)

demo = gr.ChatInterface(chat_response)



def task_1():
    demo.launch()
def task_2():
    subprocess.run("xdg-open http://127.0.0.1:7860", shell=True, capture_output=True, text=True)


thread_1 = threading.Thread(target=task_1)
thread_2 = threading.Thread(target=task_2)







def main():
    # Iniciar as threads
    thread_1.start()
    time.sleep(1)
    thread_2.start()








if __name__ == "__main__":
    main()

    


