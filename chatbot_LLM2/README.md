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
Este chatbot fornece um conjunto de orientações sobre o contexto fornecido no diretorio \chatbot_LLM2\ros2_ws\src\chat_bot\chat_bot\contexto.txt. Após a inicialização, abrirá um terminal contendo um link, após abrir esse link em seu navegador o sistema já estará apto a receber suas perguntas.
1. Inicialize o ollama server.
    ```bash
    ollama serve

2. Inicialize o chat bot.
    ```bash
    ros2 run chat_bot bot

Para visualizar o comportamento esperado, recomendamo assistir ao vídeo abaixo que demonstra o funcionamento da ferramenta:
[Assista ao vídeo de demonstração da ferramenta aqui](https://clipchamp.com/watch/FOVDab1psLs)

## Construção
### 1. Prompt de sistema
Esse bot usa algumas ferramentas da langchain para contextualizar as respostas, nesse caso o meu prompt de sistema que configura meu chat para responder questões sobre EPIs é esse:
1. template:
    ```bash
      template = """ Você é com um sistema especializado em fornecer informações concisas e precisas sobre normas de segurança em ambientes industriais. Você foi treinado para oferecer orientações relacionadas a equipamentos de          proteção individual (EPIs), práticas seguras de operação e medidas de prevenção em diversos cenários industriais. """
