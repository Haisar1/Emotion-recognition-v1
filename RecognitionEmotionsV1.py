import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imwrite("test.jpg", frame)

    try:
        result = DeepFace.analyze("test.jpg", actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']

        cv2.putText(frame, f"Emocion: {emotion}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    except:
        pass

    cv2.imshow("Detección de Emociones", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
