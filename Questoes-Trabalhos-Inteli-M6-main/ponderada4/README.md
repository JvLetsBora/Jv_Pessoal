<img src="../assets/logo-inteli.png" alt="Logo do Inteli"/>

# Ponderada 4

A aplicação é um sistema de upload e processamento de imagens, composto por um backend em FastAPI e um frontend em HTML e JavaScript.

Backend
Arquivo main.py
O arquivo main.py contém a configuração e inicialização do servidor backend usando o framework FastAPI.

include_router(app): Função auxiliar que inclui os roteadores na aplicação FastAPI.
start_application(): Função responsável por criar e retornar a instância do aplicativo FastAPI.
app: Instância do aplicativo FastAPI criada pela função start_application().
Rota /: Rota principal que retorna uma mensagem JSON.
Arquivo route_homepage.py
O arquivo route_homepage.py contém os roteadores e manipuladores de rotas relacionados às páginas da aplicação.

Image: Classe do modelo de dados que representa uma imagem com os campos name e url.
url e key: Variáveis que armazenam a URL e chave de acesso ao Supabase.
supabase: Instância do cliente Supabase criada com a URL e chave fornecidas.
image_router: Roteador do FastAPI com o prefixo "/images".
Rota /tt: Rota que retorna uma mensagem JSON.
Rota /get_all: Rota assíncrona que lista todos os arquivos em um bucket do Supabase.
Rota /get/{file}: Rota assíncrona que retorna a URL pública de um arquivo específico.
Rota /add_a: Rota assíncrona que recebe o upload de uma imagem, processa-a e a salva no Supabase.
Arquivo route_homepage.py (continuação)
general_pages_router: Roteador do FastAPI para as páginas gerais da aplicação.
Rota /: Rota que renderiza o template HTML da página inicial.
<br>
Frontend
Arquivo templates/homepage.html
O arquivo templates/homepage.html é um template HTML usado para renderizar a página inicial da aplicação.

{% extends "shared/base.html" %}: Indica que este template estende o template "shared/base.html".
{% block title %}: Bloco que define o título da página como "Job Board".
{% block content %}: Bloco que contém o conteúdo principal da página.
<div id="main">: Div que contém o cabeçalho, campo de input de arquivo e botão de envio.
<div id="img_load">: Div que será preenchida com a imagem processada.
Blocos {% endblock %}: Indicam o fim dos blocos anteriores.
Arquivo shared/base.html
O arquivo shared/base.html é um template HTML base usado como layout para todas as páginas da aplicação.

Tags <head>: Metadados, links para arquivos CSS e título da página.
Tag <style>: Estilo CSS para a exibição das imagens.
<script>: Script JavaScript contendo duas funções.
envia(): Envia o arquivo selecionado para a API e exibe a imagem processada retornada.
previewImage(): Exibe a imagem selecionada no campo de input.
Blocos {% block title %} e {% block content %}: Espaços reservados para
