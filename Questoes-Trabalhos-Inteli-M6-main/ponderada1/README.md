<img src="../assets/logo-inteli.png" alt="Logo do Inteli"/>
(https://drive.google.com/file/d/1OiihrjWdBNIjfUe8oQSwVV_JvL9dILoq/view?usp=share_link)
# Atividade 1: Turtlesim: simulando um ambiente robótico integrado no ROS

## Estrutura de pastas:
.
└── code
    ├── turtle.py
    └── requirements.txt

1 directory, 2 files
```

O arquivo `exemplo.py` é um script utilizando OOP para interagir com o nó de simulação do turtlesim. Já o requirements.txt é o resultado de um comando `pip freeze` dentro de um venv utilizado para criar esse exemplo. Isso significa que ele tem todos os pacotes necessários para rodar o script. Vamos garantir que está tudo instalado com: 

```bash
pip install -r requirements.txt
```

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

Pronto! Você já está preparado para começar a desenvolver seu autoestudo. Divirta-se! =D
