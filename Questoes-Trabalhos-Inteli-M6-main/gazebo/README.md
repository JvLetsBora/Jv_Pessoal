<table>
<tr>
</td>
<td><a  href= "https://www.inteli.edu.br/"><img  src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png"  alt="Inteli - Instituto de Tecnologia e Liderança"  border="0"  width="80%"></a>
</td>
</tr>
</table>


# Sumário
- [Autores](#autores)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Desenvolvimento](#desenvolvimento)
- [Conclusão](#conclusão)
- [Referências](#referências)


# Autor
João Vitor Oliveira Rodrigues

# Visão Geral do Projeto
## Proposta
O projeto proposto pelo Instituto de Liderança e Tecnologia - INTELI, em colaboração com o professor de programação Rodrigo Mangoni Nicola, busca proporcionar aprendizado prático aos alunos do 2º ano do curso de Engenharia da Computação. O objetivo é criar um algoritmo de rotas que possa interagir com a simulação Gazebo utilizando os princípios de nós do ROS (Robot Operating System), aplicando os conhecimentos adquiridos sobre o ambiente ROS2 e o sistema operacional Ubuntu.

## Requisitos
O enunciado dessa atividade contempla os seguintes requisitos:

Para esta atividade, espera-se a capacidade demonstrável de interagir com um ambiente de simulação de robôs, gerando um movimento controlado na plataforma turtlebot3. A entrega deve ser um vídeo demonstrando o funcionamento do projeto, um texto conciso descrevendo como foi feita a implementação e o link para o repositório público no github onde foi feita a implementação.

Padrão de qualidade:

1. Setup adequado do ambiente de simulação; (peso 1)
2. Interação adequada com os tópicos relacionados ao robô simulado; (peso 2)
3. Demonstração de movimento controlado de acordo com uma rota pré-estabelecida; (peso 3)
4. Explicação coerente e concisa da implementação (min 250 caracteres e máximo 1500); (peso 2)
5. Congruência entre o que foi escrito e o código disposto no repositório do github; (peso 2)

## Desenvolvimento
Para iniciarmos a nossa aplicação, precisamos abri o app 'Terminal' do Windows, e selecionarmos o ambiente do Ubuntu.
<center>
<img  src="img\sec_ambiente.png"  alt="Seleção do Ambiente Ubuntu"  />
</center>
**<font  size=2> Figura 1 — Selecionando Ambiente Ubuntu, Autoria Própria </font>**
<center>
<img  src="img\ambiente_1.png"  alt="Ambiente Ubuntu"  />
</center>
**<font  size=2> Figura 2 — Ambiente Ubuntu, Autoria Própria </font>**
Após abrirmos o terminal, após todas as instalações já terem sido feitas, colocamos os seguintes comandos:
Para inicializar o ambiente:
<b>source  /opt/ros/humble/setup.bash</b>
Para rodar o Turtlesim no ambiente Ubuntu:
<b>ros2 run turtlesim turtlesim_node</b>
Com isso podemos ver a simulação abrir e rodar.
<center>
<img  src="img\turtle.png"  alt="Simulação"  />
 
</center>
**<font  size=2> Figura 3 — Simulação Turtlesim, Autoria Própria </font>**
Para fazer a tartaruga se move, ela funciona por meio de requisições do Turtlesim, em suma, são mensagens ROS envidas para um nó específico que contem informações sobre velocidade, posição e orientação. Ela lê essa requisição e retorna a posição corrigida. A linguagem de programação utilizada foi Python como o nome do arquivo 'test.py'.
No código abaixo, o a linha que publica a requisição para o servidor é:
<b>linha 11___self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)</b>
Ela é resposável por enviar todas os parâmetros e o simulador interpertar e alterar as posição da tartaruga.
Ainda sobre esse tópico, o professor Rodrigo Mangoni Nicola nos enviou um código que enviar requisições constantes para o sevidor, fazendo a tartaruga se move, deixando um rastro em forma de circulo.
Abrimos 2 terminais, um que serve para rodar a aplicação gráfica, no caso a tela da tartaruga, e o segundo terminal nos rodamos o arquivo Python que contem o código com a requisição, resultando no seguinete resultado:
<center>
<img  src="img\code_circle.png"  alt="Simulação"  />
</center>
**<font  size=2> Figura 4 — Código que faz a tartatuga caminhar em circulo, Distribuído por Rodrigo Mangoni Nicola </font>**
<center>
<img  src="img\turtle_circle.png"  alt="Simulação"  />
</center>
**<font  size=2> Figura 5 — Resultado do codigo com a simulação, Distribuído por Rodrigo Mangoni Nicola </font>**
Para a nossa aplicação do projeto, o objetivo é fazer um outra figura com o rastro da tartaruga diferente do que mostrado, que no caso é o circulo.
No programa do projeto foi desenhado pelo rastro uma 'estrela', onde a lógica das requisição praticamente se mante, e umas das principais alterações que foram feitas foi na função <b>def move_turtle(self)</b>, que é a responsável por fazer a trajetória da tartaruga.
A lógica principal foi começar que ela fizesse o primeiro movimento e depois por meio de um <b>for</b> repetisse as arestas em uma angulação de 144 graus, formando assim a estrela.
Segue o código abaixo.
<center>
<img  src="img\code_estrela.png"  alt="Simulação"  />
</center>
**<font  size=2> Figura 6 — Código que faz a tartatuga caminhar em uma estrela de 5 pontos, Distribuído por Rodrigo Mangoni Nicola e alterado por Kil Matheus </font>**
A figura a seguir mostra o resultado final:
<center>
<img  src="img\turtle_estrela.png"  alt="Simulação"  />
</center>
**<font  size=2> Figura 7 — Resultado final gráfico do caminho da tartaruga, Autoria Própria</font>**
Logo abaixo segue o link para conferir o funcionamento da atividade.
https://drive.google.com/drive/folders/1kOvolLzQ_O7Zr_vZ-mhC6-eI0zbxfNca

## Conclusão
Podemos concluir que essa atividade que o objetivo de nos mostrar de maneira simulado, como seria uma programação para a movimentação de um Robô. Em uma simulação, pode trazer o conceito de aprendizagem, mas no mundo real, pode trazer grandes benefícios como por exemplo, acessar áreas de risco ou até mesmo ajuda um grande almoxerifado a locomover grande objetos de maneira eficiente.
## Referências
TEIXEIRA. Kil Matheus Gomes. Robô Digital. Repositório Github. Disponível em: [https://github.com/Kil-Matheus/Turtlesim---Desenhando-com-Caminho](https://github.com/Kil-Matheus/Turtlesim---Desenhando-com-Caminho.git). Acesso em: 24 abr. 2023.
NICOLA,  Rodrigo Mangoni (2023). Encontro 01 - Introdução à robótica móvel.pdf . Instituto de Tecnologia e Liderança - INTELI. Disponível em: https://drive.google.com/file/d/1-dI8THMPGiNdi27UYRsY-Nfjb7Ax25D-/view?usp=sharing. Acesso em: 24 abril 2023.

