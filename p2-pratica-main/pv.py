import cv2
import numpy as np

input_video = cv2.VideoCapture('/home/jv/Downloads/p2-pratica-main/assets/arsene.mp4')

# Checa se foi possivel abrir o arquivo
if not input_video.isOpened():
    print("Error opening video file")
    exit(1)
    
# Como foi possível abrir o video de entrada, vamos agora utilizar 
# essa captura para definir o tamanho do video de saida
width  = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Cria a estrutura do video de saida
# Com formato e local do arquivo de saida
# Codec utilizado
# FPS do video e
# Tamanho do video 'm', 'p', '4', 'v'
output_video = cv2.VideoWriter( '/home/jv/Downloads/p2-pratica-main/exemplos/saida/saida.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 24, (width, height))

head = None
t = 0
# Loop de leitura frame por frame
while True:
    ret, frame = input_video.read()

    if not ret:
        break
    t_frame = frame
    t_frame = cv2.cvtColor(src=t_frame, code=cv2.COLOR_BGR2GRAY)
    x = 1.4
    y = 1.4
    if t == 0:
        head = t_frame[int(40*x):int(240*x), int(450*y):int(600*y)]
    t+= 1
    filtered = cv2.matchTemplate(
        image=t_frame,
        templ=head,
        method=cv2.TM_CCOEFF_NORMED # Correlação de Pearson normalizada
    )

    detection_threshold = 0.8
    # Encontra os pontos em que o valor passa do threshold
    pontos = np.where(filtered > detection_threshold)
    # Escolhe o primeiro ponto do conjunto
    pt = pontos[1][0], pontos[0][0]
    upper_left_corner = pt
    lower_right_corner = (
    upper_left_corner[0] + head.shape[1],
    upper_left_corner[1] + head.shape[0]
    )
    cv2.rectangle(
    img=frame,
    pt1=upper_left_corner,
    pt2=lower_right_corner,
    color=(0, 0, 255), # Vermelho
    thickness=2
    )
    output_video.write(frame)
    
    cv2.imshow('Video Playback', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


output_video.release()
input_video.release()
cv2.destroyAllWindows()

