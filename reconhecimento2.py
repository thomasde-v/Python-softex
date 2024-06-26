import cv2

# Carrega o classificador pré-treinado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializa a webcam
cap = cv2.VideoCapture(0)

while True:
    # Lê o frame da webcam
    ret, frame = cap.read()

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostos no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenha um retângulo ao redor de cada rosto detectado e adiciona o nome
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'O lindo', (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Exibe o frame com os rostos detectados
    cv2.imshow('Video', frame)

    # Se a tecla 'q' for pressionada, sai do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a webcam e fecha as janelas abertas
cap.release()
cv2.destroyAllWindows()
