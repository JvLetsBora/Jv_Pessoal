# Use a imagem oficial do Node.js como base
FROM node:14

RUN mkdir app

# We create folder named build for our stuff.

WORKDIR /app

# Basic WORKDIR is just /
# Now we just want to our WORKDIR to be /build

COPY . .

# FROM [path to files from the folder we run docker run]
# TO [current WORKDIR]
# to the WORKDIR
WORKDIR app/frontend
RUN npm i
# Exponha a porta em que a aplicação Express está ouvindo 
EXPOSE 3000

# Comando para iniciar a aplicação
CMD ["node", "./frontend/server.js"]

