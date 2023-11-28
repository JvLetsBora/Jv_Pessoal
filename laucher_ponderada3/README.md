# Projeto ROS2 para Mapeamento e Navegação com NVIZ

Este é um projeto ROS2 que inclui dois conjuntos de ferramentas, um para mapeamento utilizando RVIZ e Turtlebot3 (Launcher de Mapeamento) e outro para navegação de teste (Launcher de Navegação).

## Pré-requisitos

Certifique-se de ter o ROS2 e NVIZ instalados e configurados corretamente no seu sistema. Caso contrário, siga as instruções de instalação nos links a seguir:
- [ROS 2 Installation](https://rmnicola.github.io/m8-ec-encontros/sprint1/encontro1/setup-ros)
- [NVIZ Installation](https://rmnicola.github.io/m8-ec-encontros/sprint2/encontro4/nav2)

## Passos para Inicialização do Projeto:

1. Clone este repositório:

   ```bash
   git clone https://github.com/JvLetsBora/Jv_Pessoal.git
   cd Jv_Pessoal/laucher_ponderada3/ros2_ws


2. Construa o projeto:

    ```bash
    colcon build


3. Ative o ambiente:

    ```bash
    source install/setup.bash

Agora seu sistema já reconhece os comandos e pacotes dessa aplicação.

## Uso
Para o uso dessas ferramentas certifique-se de estar no diretório correto:
1. Entrar no diretório de laçamentos.
    ```bash
    cd src/my_package/launch

### Launcher de Mapeamento
Este launcher abrirá três ferramentas na sua tela, uma para mapeamento, outra para controle do robô e o ambiente de simulação Gazebo.

1. Para inicializar o mapeamento e geração do mapa.
    ```bash
    ros2 launch map_launch.py

### Launcher de Navegação
Após a execução desse launch, o Gazebo e o NVIZ serão inicializados, e um terceiro terminal executará um comando com coordenadas para testar seu NVIZ. Se tudo estiver instalado e configurado corretamente, o robô começará a se mover.

1. Para inicializar a navegação teste.
    ```bash
    ros2 launch map_launch.py


Para visualizar o comportamento desejado, recomendamos assistir ao vídeo abaixo que demonstra o funcionamento do mapeamento::
[Assista ao vídeo de demonstração do mapeamento aqui](https://drive.google.com/file/d/17IQbyCZW2-DupMsvM5Pft-qFq78kt6Y1/view?usp=sharing)
