# Chat bot
Este é um projeto ROS2 que inclui um pacote para robô de serviço.
## Pré-requisitos
Certifique-se de que o ROS2, a biblioteca OpenAI, gradio e o Langchain estejam instalados e configurados corretamente em seu sistema. Caso contrário, siga as instruções de instalação nos seguintes links:
- [ROS 2 instalação](https://rmnicola.github.io/m8-ec-encontros/sprint1/encontro1/setup-ros)
- [OpenAI instalação](https://platform.openai.com/docs/quickstart?context=python)
- [Gradio instalação](https://www.gradio.app/guides/quickstart)
- [Langchain instalação](https://python.langchain.com/docs/get_started/installation)
## Passos para Inicialização do Projeto:
1. Clone este repositório:
   ```bash
   git clone https://github.com/JvLetsBora/Jv_Pessoal.git
   cd Jv_Pessoal/'chatbot_LLM'/ros2_ws
2. Exporte como variável de ambiente sua chave OpenAI:
    ```bash
    export OPENAI_API_KEY='< sua chave da OpenAI >'
3. Construa o projeto:
    ```bash
    colcon build
4. Ative o ambiente:
    ```bash
    source install/setup.bash
Agora seu sistema já reconhece os comandos e pacotes dessa aplicação.
## Uso
Para o uso dessa ferramenta siga as etapas abaixo:
### Chat bot
Este chatbot fornece um conjunto de orientações sobre Equipamentos de Proteção Individual (EPIs) utilizados em diferentes áreas de atuação. Após a inicialização, abriram-se duas abas em seu computador: uma contendo o terminal de execução desse nó e uma guia do seu navegador. Após abertas, é só fazer perguntas ao chatbot.
1. Inicialize o chat bot.
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
