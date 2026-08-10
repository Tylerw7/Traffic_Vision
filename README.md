# OpenCV Traffic Detection

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red?logo=opencv&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-11-green)

A simple computer vision project using **Python, OpenCV, and YOLO11** to detect objects in a traffic video.

## Features

* Detects objects using YOLO11
* Draws bounding boxes around:

  * 🚗 Cars — Green
  * 🚌 Buses — Blue
  * 👤 People — Red
* Displays confidence scores
* Processes video frame-by-frame

## Requirements

```bash
pip install opencv-python ultralytics
```

## Run

Place `sf_traffic.mp4` in the project directory and run:

```bash
python main.py
```

Press **Q** to quit.
