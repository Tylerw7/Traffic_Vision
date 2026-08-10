import cv2
from ultralytics import YOLO


# Load YOLO model
model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture("sf_traffic.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)

delay = int(700 / fps)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)
    result = results[0]

    for box in result.boxes:
        # Get class ID
        class_id = int(box.cls[0])
        # Get class name
        class_name = model.names[class_id]
        # Get confidence
        confidence = float(box.conf[0])
        # Get bounding box coordinates
        x1,y1,x2,y2 = map(int, box.xyxy[0])

        if class_name == "car" or class_name == "bus" or class_name == "person":
            
            if class_name == "car": color = (0,255,0)
            if class_name == "bus": color = (255,0,0)
            if class_name == "person": color = (0,0,255)
            cv2.rectangle(
                frame,
                (x1,y1),
                (x2,y2),
                color,
                2
            )

        label = f"{class_name} {confidence:.2f}"

        # Draw Label
        cv2.putText(
            frame,
            label,
            (x1,y1 -10),
            cv2.FONT_HERSHEY_COMPLEX,
            0.7,
            color,
            2
        )    



    cv2.imshow("Traffic", frame)
    if cv2.waitKey(delay) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()    