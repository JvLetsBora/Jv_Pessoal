<table>
<tr>
</td>
<td><a  href= "https://www.inteli.edu.br/"><img  src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png"  alt="Inteli - Instituto de Tecnologia e Liderança"  border="0"  width="80%"></a>
</td>
</tr>
</table>
<font  size="20"><center>
Concepção de integração de aplicações
 
</center></font>
# **Sumário**
- [Autores](#autores)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Objetivos](#objetivos)
- [Instalação de Ambiente](#instalação-de-ambiente)
- [Desenvolvimento](#desenvolvimento)
- [Conclusão](#conclusão)
- [Referências](#referências)


# Autores
Kil Matheus Gomes Teixeira


# Visão Geral do Projeto
## Proposta
A fim de proporcionar aprendizado prático aos alunos do 2º ano do curso de Engenharia da Computação, o Instituto de Liderança e Tecnologia - INTELI, juntamente com o professor de programação Rodrigo Mangoni Nicola, propôs uma atividade desafiadora que busca aplicar os conhecimentos adquiridos sobre ambiente ROS2 (Ambiente de Programação de Desenvolvimento de Sistemas Robóticos) e Ubuntu.

# Objetivos
O exercício chamado de 'Turtlesim: simulando um ambiente robótico integrado no ROS', tem como objetivo principal conseguir executar os todos  ambientes de desenvolvimento, na qual o rastro da tartaruga faça um desenho.
## Requisitos
Segundo o card do AdaLove do prof. Rodrigo Mangoni Nicola, os requisitos são descricos como seguintes:
Padrão de qualidade:
Ao teerminar está atividade, espera-se que os estudantes consigam validar suas instalações locais do ambiente de desenvolvimento que será utilizado ao longo do semestre. Com sua finalização, os estudantes deverão adicionar um link para um vídeo não listado no Youtube com a simulação funcionando.
a) Configuração adequada do ambiente de desenvolvimento ROS; (peso 2)
b) Funcionamento correto do script de interação com o turtlesim; (peso 3)
c) Explicação coerente e concisa da implementação; (peso 3)
d) Congruência entre o que foi escrito e o código disposto no repositório do github; (peso 2)
## Instalação de Ambiente
A instalação do ambiente é necessária pois a nossa simulação será feita no ambiente Linux e não em um ambiente Windows nativo. Todos os programas e apps necessários estão listados abaixo. Seguindo todos os tutoriais me maneira correta, pode-se considerar que o ambiente para o desenvolvimento está concluido.
### Ubuntu 22.04.2 LTS
O aplicativo Ubuntu no Windows é uma implementação do Windows Subsystem for Linux (WSL), que permite a instalação e execução do Ubuntu no sistema operacional Windows.
O Download do Ubuntu 22.02.2 LTS pode ser feita pela Microsoft Store pelo link:
https://www.microsoft.com/store/productId/9PN20MSR04DW
O tutorial de instalação pode ser feita pelo link abaixo:
https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#2-install-wsl
*Nota: O tutorial mostra uma outra versão do aplicativo Ubuntu, mas idependente da versão, a instalação segue os mesmos passos. Vale ressaltar que a versão indicada é possui uma maior compatibilidade para o projeto. Durante ainda a instalação do sistema, é necessário cirar um perfil com nome e senha para que a palicação funcione sem mais complicações.
### ROS2
É uma aplicação para o desenvolviemento de código aberto para construir sistemas robóticos avançados. Ele consegue integrar uma variedade de componentes de hardware e software de forma simplificada.
Após a instalação completa do Ubuntu, abra o aplicativo do 'Terminal' e selecione o 'Ubuntu 22.02.2 LTS'
O tutorial para a instalação do ROS2 segue no link abaixo:
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
*Nota: No Terminal já configurado, copie e cole os comandos como está no tutorial e espere até toda a instalação seja concluida. Os tópicos a serem instalados são 'Set locale', 'Setup Souces' e 'Install ROS2 packages'. Para testar se a instalação foi feita corretamente, sempre rode o codigo que está em 'Environment Setup' e depois os de 'Try some examples'.
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
https://drive.google.com/file/d/1mlPCqhb1jqlHhZ1le4YVIU_54lTdiejy/view?usp=sharing
## Conclusão
Podemos concluir que essa atividade que o objetivo de nos mostrar de maneira simulado, como seria uma programação para a movimentação de um Robô. Em uma simulação, pode trazer o conceito de aprendizagem, mas no mundo real, pode trazer grandes benefícios como por exemplo, acessar áreas de risco ou até mesmo ajuda um grande almoxerifado a locomover grande objetos de maneira eficiente.
## Referências
TEIXEIRA. Kil Matheus Gomes. Robô Digital. Repositório Github. Disponível em: [https://github.com/Kil-Matheus/Turtlesim---Desenhando-com-Caminho](https://github.com/Kil-Matheus/Turtlesim---Desenhando-com-Caminho.git). Acesso em: 24 abr. 2023.
NICOLA,  Rodrigo Mangoni (2023). Encontro 01 - Introdução à robótica móvel.pdf . Instituto de Tecnologia e Liderança - INTELI. Disponível em: https://drive.google.com/file/d/1-dI8THMPGiNdi27UYRsY-Nfjb7Ax25D-/view?usp=sharing. Acesso em: 24 abril 2023.
# Agradecimentos
Agradecimentos especiais a:
 Rodrigo Mangoni Nicola pelo seu grande conhecimento em programação que sempre nos ajuda em todos os desenvolvimentos.
