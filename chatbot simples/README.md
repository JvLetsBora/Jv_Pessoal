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

### 1.  Dicionários internos
Das possibilidades de inteções as que se refere a soliciar uma ferramenta tem como resultado a função 'control', agora as intenções de achar um setor levam para a função 'go_to'.

1. intenções
    ```python
    intent_dict = {
        r"\b^([Qq]uero|[Pp]reciso|[Ee]stou|[Oo]nde encontro|[Pp]rocuro)\s+[a-zA-Z\s]+\s(.+)$":control,
        r"\b[Vv][áa](?:\spara)?\s?[oa]?\s(.+)":go_to,
        r"\b[Mm]e\sleve até\s?[oa]?\s(.+)":go_to
        }


Para a função control os possiveis resultados estão descritos no dicionário 'point_dict', enquanto para função go_to estão descritos no dicionário 'area_dict':
2. ações
    ```python
    point_dict = {
        r"martelo": (area_dict['setor a'],"Setor A"),
        r"marreta": (area_dict['setor b'],"Setor B"),
        r"prego": (area_dict["setor a"],"Setor A"),
        r"porca": (area_dict["setor d"],"Setor D"),
        r"chave de Fenda": (area_dict["setor c"],"Setor C"),
        r"alicate": (area_dict["setor a"],"Setor A"),
        r"chave Inglesa": (area_dict["setor c"],"Setor C"),
        r"parafuso": (area_dict["setor a"],"Setor A"),
        r"serra": (area_dict['setor b'],"Setor B"),
        r"lixa": (area_dict["setor d"],"Setor D"),
    }
    area_dict = {
        "setor a": (0.0, 2.0, 0.0, 1.0, 0.0, 0.0),
        "setor b": (60.0, 0.0, 0.0, 1.0, 0.0, 0.0),
        "setor c": (0.0, 0.2, 0.0, 1.0, 0.0, 0.0),
        "setor d": (5.0, 0.0, 0.0, 1.0, 7.0, 0.0)
    }