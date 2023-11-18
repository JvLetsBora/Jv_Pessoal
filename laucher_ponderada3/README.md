# Projeto ROS2 para mapeamento e navegação com NVIZ

Este é um projeto ROS2 que inclui dois conjuntos de ferramentas, uma para mapeamento utilizando RVIZ e Turtlebot3 (Launcher de Mapeamento) e outro para navegação teste (Launcher de Navegação).

## Pré-requisitos

Certifique-se de ter o ROS2 e NVIZ instalado e configurado corretamente no seu sistema. Caso contrário, siga as instruções de instalação nos links a seguir: [ROS 2 Installation](https://rmnicola.github.io/m8-ec-encontros/sprint1/encontro1/setup-ros)

[NVIZ](https://rmnicola.github.io/m8-ec-encontros/sprint2/encontro4/nav2)


## Instalação

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

## Uso
### Launcher de Mapeamento
1. Para inicializar o mapeamento e geração do mapa.
    ```bash
    cd src/my_package/launch
    ros2 launch map_launch.py

### Launcher de Navegação
1. Para inicializar a navegação teste.
    ```bash
    cd src/my_package/launch
    ros2 launch map_launch.py