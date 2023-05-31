<img src="../assets/logo-inteli.png" alt="Logo do Inteli"/>


<br>
#Código para Treinamento com YOLO
<p>Este código realiza o treinamento de um modelo YOLO utilizando a biblioteca Ultralytics e a API Roboflow. O YOLO (You Only Look Once) é um framework de detecção de objetos em imagens amplamente utilizado em visão computacional.</p>

##Instalação de Dependências
<p>O código inicia instalando as seguintes bibliotecas através do comando pip install:
<br>
Ultralytics: Essa biblioteca é instalada usando o comando !pip install ultralytics. Ela fornece suporte ao framework YOLO e será utilizada posteriormente no treinamento do modelo.
Roboflow: A biblioteca Roboflow é instalada com o comando !pip install roboflow. Ela é utilizada para trabalhar com conjuntos de dados de visão computacional.
Utilização do YOLO
  <br>
O código utiliza o comando !yolo help para exibir informações de ajuda sobre o YOLO. Isso permite ao usuário obter detalhes sobre os comandos e opções disponíveis para uso.
</p>
##Configuração do Roboflow
<p>O código importa a classe Roboflow da biblioteca Roboflow e cria uma instância chamada rf. Essa instância é inicializada com uma chave de API fornecida no parâmetro api_key. Essa chave de API é usada para autenticar a conexão com a API do Roboflow.

Em seguida, o código utiliza a instância rf para acessar um projeto específico no espaço de trabalho do Roboflow. O projeto é chamado "crack-bphdr" e está localizado no espaço de trabalho "university-bswxt". A API do Roboflow é utilizada para acessar esse projeto.

Download do Conjunto de Dados
Através da instância project, o código acessa a versão 2 do projeto e realiza o download de um conjunto de dados chamado <b>"yolov8"</b> usando o método download. Esse conjunto de dados provavelmente contém imagens e anotações associadas utilizadas para treinar um modelo YOLO.
</p>

##Treinamento do Modelo YOLO
<p>O código finalmente inicia o treinamento do modelo YOLO utilizando o comando !yolo train. Os parâmetros fornecidos para o treinamento são os seguintes:
<br>
data=/content/crack-2/data.yaml: Especifica o caminho para o arquivo de configuração data.yaml. Esse arquivo contém informações sobre o conjunto de dados, como a localização das imagens e anotações.
model=yolov8n.pt: Especifica o modelo a ser utilizado no treinamento. Nesse caso, o modelo YOLOv8n é utilizado.
epochs=10: Define o número de épocas para o treinamento. O modelo será treinado por 10 épocas.
lr0=0.01: Define a taxa de aprendizado inicial do treinamento.
É importante observar que os comandos iniciados com "!" são executados como comandos de terminal dentro do ambiente de execução onde o código está sendo executado.
</p>
