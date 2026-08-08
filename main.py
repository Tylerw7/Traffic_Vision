import cv2

cap = cv2.VideoCapture("sf_traffic.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)

delay = int(700 / fps)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Traffic", frame)
    if cv2.waitKey(delay) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()    