# Chat bot com RAG
Este é um projeto ROS2 que inclui um pacote para robô de serviço com integração de contexto.
## Pré-requisitos
Certifique-se de que o ROS2, o Ollama, gradio e o Langchain estejam instalados e configurados corretamente em seu sistema. Caso contrário, siga as instruções de instalação nos seguintes links:
- [ROS 2 instalação](https://rmnicola.github.io/m8-ec-encontros/sprint1/encontro1/setup-ros)
- [Ollama](https://ollama.ai)
- [Gradio instalação](https://www.gradio.app/guides/quickstart)
- [Langchain instalação](https://python.langchain.com/docs/get_started/installation)
## Passos para Inicialização do Projeto:
1. Clone este repositório:
   ```bash
   git clone https://github.com/JvLetsBora/Jv_Pessoal.git
   cd Jv_Pessoal/'chatbot_LLM2'/ros2_ws
2. Construa o projeto:
    ```bash
    colcon build
3. Ative o ambiente:
    ```bash
    source install/setup.bash
Agora seu sistema já reconhece os comandos e pacotes dessa aplicação.
## Uso
Para o uso dessa ferramenta siga as etapas abaixo:
### Chat bot
Este chatbot fornece um conjunto de orientações com base no contexto fornecido no diretório 
\chatbot_LLM2\ros2_ws\src\chat_bot\chat_bot\contexto.txt.

Para utilizar o chatbot, siga estas instruções:
1. Inicialize o ollama server.
    ```bash
    ollama serve

2. Em outro terminal para iniciar o chat bot rode:
    ```bash
    ros2 run chat_bot bot

Lembre-se de consultar o arquivo contexto.txt para obter informações sobre o contexto atual do chatbot.

Para visualizar o comportamento esperado, recomendamo assistir ao vídeo abaixo que demonstra o funcionamento da ferramenta:
[Assista ao vídeo de demonstração da ferramenta aqui](https://clipchamp.com/watch/FOVDab1psLs)

## Construção

### 1. Configuração do Contexto

Este bot utiliza ferramentas da LangChain para contextualizar as respostas. Para compreender melhor o seu funcionamento, siga os passos abaixo:

**1.1. Acesse o Módulo chain.py:**

1. Abra o terminal e navegue até o diretório `chat_bot`:
    ```bash
    cd src/chat_bot/chat_bot/

