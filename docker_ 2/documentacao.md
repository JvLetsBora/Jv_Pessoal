# Todolist Docker-Compose

## Estrutura de Pastas
A realização desse projeto foi dividida em:

- **/code**: Pasta que contem a aplicação "app" na qual a imagem todolist foi criada.
- - **/code/dockerfile**: Arquivo que cria a imagem.
- - **/code/app**: Código da aplicação que estruturou a imagem todolist.
- **docker-compose.yml**: Arquivo responsável por subir a aplicação.

## Pré-requisitos
Para rodar essa aplicação é necessário ter o docker instalado.

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

**Caso apareça o erro:** <br>
(node:1) UnhandledPromiseRejectionWarning: Error: connect ECONNREFUSED 172.19.0.2:5432
<br>
- Pare a aplicação com as teclas "control + c" ou dei o comando stop nos conteners dessa aplicação.
- Execulte novamente o comando "docker compose up".

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
