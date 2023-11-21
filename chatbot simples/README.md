# Chat bot 

Este é um projeto ROS2 que inclui um pacote para robô de serviço.

## Pré-requisitos

Certifique-se de ter o ROS2 instalados e configurados corretamente no seu sistema. Caso contrário, siga as instruções de instalação nos links a seguir:
- [ROS 2 Installation](https://rmnicola.github.io/m8-ec-encontros/sprint1/encontro1/setup-ros)

## Passos para Inicialização do Projeto:

1. Clone este repositório:

   ```bash
   git clone https://github.com/JvLetsBora/Jv_Pessoal.git
   cd Jv_Pessoal/'chatbot simples'/ros2_ws


2. Construa o projeto:

    ```bash
    colcon build


3. Ative o ambiente:

    ```bash
    source install/setup.bash

Agora seu sistema já reconhece os comandos e pacotes dessa aplicação.

## Uso
Para o uso dessas ferramenta siga as etapas abaixo:

### Chat bot 
Esse chat bot reconhe três tipos de comando:
-  Para achar uma ferramenta use: 'quero', 'preciso', 'estou' ou 'onde encontro'
-  Para achar um setor: 'vá para' ou 'me leve'.
-  Para finalizar o chat: "sair"

1. Inicialize o chat bot.
    ```bash
    ros2 run chat_bot bot

Agora ele está apto para receber as instruções.



## Construção

### Dicionário de interação
1. Inicialize o chat bot.
    ```python
    intent_dict = {
        r"\b^([Qq]uero|[Pp]reciso|[Ee]stou|[Oo]nde encontro|[Pp]rocuro)\s+[a-zA-Z\s]+\s(.+)$":control,
        r"\b[Vv][áa](?:\spara)?\s?[oa]?\s(.+)":go_to,
        r"\b[Mm]e\sleve até\s?[oa]?\s(.+)":go_to
        }
