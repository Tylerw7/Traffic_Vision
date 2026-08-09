from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("sf_traffic.mp4")
result = results[0]

print(result.boxes)
