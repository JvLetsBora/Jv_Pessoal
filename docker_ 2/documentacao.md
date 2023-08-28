# Todolist Docker-Compose

## Estrutura de Pastas
A realização desse projeto foi dividida em:

- **/docs**: Contém a documentação do projeto.
- **/src**: Contém o código-fonte principal.
- **/public**: Contém arquivos públicos, como imagens ou recursos estáticos.
- **/tests**: Contém os testes automatizados.
- **/config**: Contém configurações do projeto.
- **/scripts**: Contém scripts de utilidade para tarefas comuns.
- **/dist**: Contém os arquivos gerados após a compilação ou construção do projeto.

## Pré-requisitos
Liste todos os pré-requisitos necessários para executar o projeto. Isso pode incluir linguagens de programação, bibliotecas, ferramentas ou serviços específicos.

## Arquitetura da solução
O projeto foi dividido em dois contêineres devido à minha falta de familiaridade com a conternização. As partes descritas no arquivo docker-compose.yml, localizado neste diretório, são as seguintes:

### Container do Banco de Dados (DB): 
Este contêiner utiliza uma imagem oficial do PostgreSQL para armazenar os dados do aplicativo.

### Container do Adminer: 
Este contêiner carrega minha aplicação web chamada "todolist" diretamente do Docker Hub.


## Instruções para Iniciar a Aplicação
Para garantir o funcionamento adequado desta aplicação, siga estas etapas:

Abra o terminal na pasta "docker_2" <br>
Defina esta pasta como o diretório raiz. <br>
Execute o comando "docker-compose up" para inicializar a aplicação.

## Instruções de Uso
Após concluir os passos descritos na seção "Instruções para Iniciar a Aplicação", a aplicação web estará disponível em: http://localhost:3000/.

### Login
Para acessar a aplicação, é necessário efetuar o login. Você pode usar as seguintes credenciais de teste:

Login: teste <br>
Senha: teste123

### Criar uma Nota
Nesta parte da aplicação, é possível adicionar uma nota e um título para essa nota usando os campos no centro da parte superior da tela. Após preencher os campos, basta clicar no botão "Confirmar" para adicionar sua nota.

### Deletar uma Nota
Para excluir uma nota, simplesmente clique no ícone de lixeira localizado no cartão da nota desejada. É importante notar que essa ação requer uma confirmação antes de ser efetivamente executada.

### Atualizar uma Nota
Para atualizar uma nota, clique no ícone de lápis presente no cartão da nota. Isso abrirá um modal com um campo de entrada semelhante ao usado para criar uma nova nota. O processo de atualização é semelhante ao de criação de uma nova nota.

## Estrutura do Banco de Dados
Esta aplicação utiliza as seguintes tabelas:

### Tabela "main"
Esta tabela é responsável por armazenar as notas do usuário. Elas são registradas nas colunas "titulo" e "body".

### Tabela "users"
Esta tabela é responsável por armazenar as credenciais do usuário. As informações são registradas nas colunas "username" e "password".

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
