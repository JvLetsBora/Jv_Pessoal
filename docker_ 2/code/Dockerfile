# Use a imagem oficial do Node.js como base
FROM node:14

# Crie e defina o diretório de trabalho no contêiner
WORKDIR /code/

# Copie todo o conteúdo do diretório 'app' do host para o diretório de trabalho no contêiner
COPY app ./app

# Exponha a porta em que a aplicação Express está ouvindo 
EXPOSE 3000

# Comando para iniciar a aplicação
CMD ["node", "app/backend/index.js"]
