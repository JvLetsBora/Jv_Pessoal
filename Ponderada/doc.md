# App com I.A

## Estrutura de Pastas

- **/app**: Aplicação "app" na qual a imagem todolist foi criada.
- - **/app/Activity_history.csv**: Dados base usado para o treino de modelo.
- - **/app/dockerfile**: Arquivo que cria a imagem.
- - **/app/main.py**: Arquivo que contém as regras da API.
- - **/app/ponderada3.py**: Arquivo que contém o processamento e treinamento do modelo, bem como o modelo treinado.
- - **/app/requirements.txt**: Arquivo usado para descrever as dependências desse projeto.


## Pré-requisitos
Para rodar essa aplicação é necessário ter o docker instalado.

## Instruções para Iniciar a Aplicação
Para garantir o funcionamento adequado desta aplicação, siga estas etapas:

- Abra o terminal na pasta "Ponderada/app" <br>
- Defina esta pasta como o diretório raiz. <br>
- Execute o comando "docker push jvdev68/podia" para baixar a imagem do DockerHub. <br>
- Execute o comando "docker run -p 80:8000 jvdev68/podia" para inicializar a aplicação.

## Instruções de Uso
Após concluir os passos descritos na seção "Instruções para Iniciar a Aplicação", a API estará disponível em: http://localhost:8000/.

### Serviços:

- **Fazer a predição de tempo de uso de um desses aplicativos:  "WhatsApp", "Instagram", "Gmail", "YouTube", baseado na hora do dia**
Para isso será necessario fazer um post para rota: "http://localhost:8000/"

Exemplo do formato de dado suportado pela a API:

{ <br>
  "Time": "00:00:00 am",            <br>
  "WhatsApp": 0,                    <br>
  "Instagram": 0,                   <br>
  "Gmail": 1,                       <br>
  "YouTube": 0                      <br>
}

**Time**, esse atributo deve seguir a formatação hora:minuto:segundo sendo obrigatório ter ou **am** ou **pm** no final. <br>
**WhatsApp**, esse atributo deve seguir a formatação booleana de 0 ou 1, indicando se é o target ou não. <br>
**Instagram**, esse atributo deve seguir a formatação booleana de 0 ou 1, indicando se é o target ou não. <br>
**Gmail**, esse atributo deve seguir a formatação booleana de 0 ou 1, indicando se é o target ou não. <br>
**YouTube**, esse atributo deve seguir a formatação booleana de 0 ou 1, indicando se é o target ou não. <br>
