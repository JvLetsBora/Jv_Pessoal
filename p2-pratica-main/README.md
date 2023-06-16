# Documentação do que foi feito

## pv.py
Esse é o arquivo principal, é nele que é feita a leitura e tratamento dos frame e a geração de um novo video. 

## Leitura de video

Dentro de um loop while o video é aberto, a função responsavel por fazer essa leitura 'read()' que retorna cada frame de do video, para cada frame do video aplico uma transfomação no canal de cores, deixando os em uma escala de cinza e salvo na variavel t_frame. Com o primeiro frame em mão eu faço um recorte da minha area de interesse e salvo na variavel head. Utilizando uma blibioteca aplico um filtro de covolução comparando minha variavel t_frame com a head, e para toda comparação que der mais de 7.9, desenho um retangulo no frame na area da cabeça. Ao final de cada passada do loop salvo o frame, que agora tem o desenho de um retangulo, em um arquivo de video.

## Geração de um novo video
Para isso crio um arquivo em branco no formato mp4 que é populado com frames a cada passada do loop mencionado acima.

