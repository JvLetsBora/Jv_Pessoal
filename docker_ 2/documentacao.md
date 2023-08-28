## Arquitetura da solução
O projeto foi dividido em dois contêineres devido à minha falta de familiaridade com a conternização. As partes descritas no arquivo docker-compose.yml, localizado neste diretório, são as seguintes:

### Container do Banco de Dados (DB): 
Este contêiner utiliza uma imagem oficial do PostgreSQL para armazenar os dados do aplicativo.

### Container do Adminer: 
Este contêiner carrega minha aplicação web chamada "todolist" diretamente do Docker Hub.


## Instruções para lançar a aplicação
Para o funcionamento dessa aplicação será necessario a abertura da pasta code inicia-la com o comando docker-compose up

Este repositório contém uma aplicação web contida, onde utilizei o Uvicorn para servir uma página da web e o Docker para criar uma imagem e containerizar a aplicação. Durante a criação da imagem, baseei-me na versão python:3.9.4-buster e utilizei as ferramentas especificadas no arquivo requirements.txt para garantir todas as dependências necessárias. A estrutura do Dockerfile e do arquivo main.py foi planejada da seguinte forma:
### Definindo a imagem base
FROM python:3.9.4-buster

### Criando uma pasta chamada 'build' para nossos arquivos
RUN mkdir build

### Definindo o diretório de trabalho como '/build'
WORKDIR /build

### Copiando todos os arquivos do contexto (pasta local) para o diretório de trabalho
COPY . .

### Instalando as dependências especificadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

### Expondo a porta 80 para o tráfego
EXPOSE 80

### Definindo o diretório de trabalho como '/build/app'
WORKDIR /build/app

### Iniciando o servidor Uvicorn com as configurações adequadas
CMD python -m uvicorn main:app --host 0.0.0.0 --port 80


## Sobre aplicação que foi empacotada:
Nesta solução, a aplicação FastAPI é servida pelo Uvicorn, enquanto o Docker é usado para empacotar a aplicação em uma imagem contida, facilitando a implantação consistente e isolada.
