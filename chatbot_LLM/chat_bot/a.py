import threading
import time

def task_1():
    for i in range(5):
        print(f"Task 1: {i}")
        time.sleep(1)

def task_2():
    for i in range(5):
        print(f"Task 2: {i}")
        time.sleep(1)

# Criar instâncias de threads
thread_1 = threading.Thread(target=task_1)
thread_2 = threading.Thread(target=task_2)

# Iniciar as threads
thread_1.start()
thread_2.start()

# Aguardar até que ambas as threads terminem
#thread_1.join()
#thread_2.join()

print("Ambas as threads concluídas.")
