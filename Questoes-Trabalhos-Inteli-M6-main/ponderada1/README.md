<img src="../assets/logo-inteli.png" alt="Logo do Inteli"/>

# Atividade 1: Turtlesim: simulando um ambiente robótico integrado no ROS

**Conteúdo**

- [Estrutura de pastas](#Estrutura-de-pastas)
- [Funcionamento](#Funcionamento)
- [Descrição do código](#Descrição-do-código)
  - [Criando um nó](#Criando-um-nó)
  - [Inicialização](#Inicialização)
- [Referências](#Referências)


## Estrutura de pastas:
.
└── code
    ├── turtle.py
    └── requirements.txt

1 directory, 2 files
```
O arquivo `turtle.py` é um script utilizando OOP para interagir com o nó de simulação do turtlesim. Já o requirements.txt é o resultado de um comando `pip freeze` dentro de um venv utilizado para criar esse exemplo. Isso significa que ele tem todos os pacotes necessários para rodar o script. Vamos garantir que está tudo instalado com: 
```

```
bash
pip install -r requirements.txt
```

## Funcionamento
Siga as intruções para rodar o exemplo.
OK! Agora estamos prontos para rodar o exemplo. Primeiro, abra um terminal e rode o comando necessário para inicializar o nó do turtlesim:
```bash
ros2 run turtlesim turtlesim_node
```

A seguir, basta rodar o script em outro terminal. Para isso, primeiro vamos garantir que ele está com permissão para execução:

```bash
chmod +x exemplo.py
```

Ok, agora basta rodar o script como se fosse um executável qualquer em Linux:

```bash
./exemplo.py
```
Com tudo rodando o comportamento deve ser igual a esse:
[Video do funcionamento](https://drive.google.com/file/d/1OiihrjWdBNIjfUe8oQSwVV_JvL9dILoq/view?usp=share_link)


## Descrição do código

Antes de começar as seguintes importações são necessárias para a comunicação com o nó:
```
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
```

### Criando um nó
A classe TurtleController herda Node o que possibilita que ela se comporte como um nó.
```class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.move_turtle)
        self.twist_msg_ = Twist()
        self.x = 0

    def move_turtle(self):
        if self.x < 2:
            self.x += 0.05
        else:
            self.x -= 3.0
        self.twist_msg_.linear.x = 1.0 + self.x
        self.twist_msg_.angular.z = self.x
        self.publisher_.publish(self.twist_msg_)

```

Essa linha é responsável criar uma comunicação com o tópico 'turtle1/cmd_vel'.
```
self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
```

Essa linha é responsável por criar um loop que é exucuta a cada 1 segundo a função move_turtle:
```
self.timer_ = self.create_timer(0.1, self.move_turtle)
```
A função move_turtle é responsável por váriar os valores linear.x, responsável pela movimentação da tartaruga e angular.z, responsável pela inclinação da tartaruga. Com uma lógica simples de if e else essa função soma em self.x 0.05 a cada vez que é chamada, ao atingir um valor superior a 2 execulta o código do else que básicamente faze com que self.x sejá -3 o que gera um loop de movimento, formando uma função que ocila de -3 a 2.

Após as váriações serem registradas em twist_msg_ em self.publish essas alterações são enviadas:
```
self.publisher_.publish(self.twist_msg_)
```
### Inicialização

Em main é feita a instâncialização da classe "TurtleController" e a criação da comunicação. 
```
def main(args=None):
    rclpy.init() # Inicializa o rclpy
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller) # Função que executa um Node
    turtle_controller.destroy_node() # Função que destroi o Node
    rclpy.shutdown() #Função que encerra a aplicação
    
```

Essa linha é padrão em uma aplicação python, sendo responsável por inicializar a função main(), descrita acima.
```
if __name__ == '__main__':
    main()
```

## Referências:
[Documentação ROS2](https://docs.ros2.org/foxy/api/rclpy/api/)

[Exemplo que me Baseei](https://github.com/Murilo-ZC/Questoes-Trabalhos-Inteli-M6/tree/main/ponderada1)
