import cv2
import mediapipe as mp

# Inicializações
video = cv2.VideoCapture(0)
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Variáveis
linha_x = 800  # Linha vertical no meio da imagem (ajuste conforme necessário)
entradas = 0
saidas = 0
estado_anterior = {}

# Função para determinar a direção com base no eixo X
def detectar_direcao(id_pessoa, pos_atual_x):
    if id_pessoa not in estado_anterior:
        estado_anterior[id_pessoa] = pos_atual_x
        return None

    pos_anterior_x = estado_anterior[id_pessoa]
    estado_anterior[id_pessoa] = pos_atual_x

    if pos_anterior_x < linha_x and pos_atual_x >= linha_x:
        return 'entrou'  # Da esquerda para direita
    elif pos_anterior_x > linha_x and pos_atual_x <= linha_x:
        return 'saiu'    # Da direita para esquerda
    return None

# Loop principal
id_pessoa = 0  # Simulação de ID (MediaPipe não fornece múltiplos IDs por padrão)
while True:
    check, img = video.read()
    if not check:
        break

    img = cv2.resize(img, (1600, 900))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resultados = pose.process(img_rgb)

    if resultados.pose_landmarks:
        lm = resultados.pose_landmarks.landmark

        quadril_direito = lm[24]
        quadril_esquerdo = lm[23]

        # Coordenadas médias (ponto central entre os quadris)
        cx = int(((quadril_direito.x + quadril_esquerdo.x) / 2) * img.shape[1])
        cy = int(((quadril_direito.y + quadril_esquerdo.y) / 2) * img.shape[0])

        direcao = detectar_direcao(id_pessoa, cx)
        if direcao == 'entrou':
            entradas += 1
        elif direcao == 'saiu':
            saidas += 1

        # Desenhar ponto
        cv2.circle(img, (cx, cy), 10, (255, 0, 0), -1)

        # Desenhar landmarks
        mp_draw.draw_landmarks(img, resultados.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Desenhar linha de entrada/saída (vertical)
    cv2.line(img, (linha_x, 0), (linha_x, img.shape[0]), (0, 255, 0), 2)

    # Exibir contadores
    cv2.putText(img, f'Entradas: {entradas}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 128, 0), 2)
    cv2.putText(img, f'Saidas: {saidas}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Mostrar imagem
    cv2.imshow('Contador de Pessoas', img)

    # Tecla ESC para sair
    if cv2.waitKey(30) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()
