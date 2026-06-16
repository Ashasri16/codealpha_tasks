# Object Detection and Tracking

## About the Project

This project was developed as part of the CodeAlpha Artificial Intelligence Internship.

The project uses YOLOv8 and OpenCV to perform real-time object detection and tracking through a webcam. It detects objects in the video stream, draws bounding boxes around them, and tracks them as they move.

## Features

- Real-time object detection
- Real-time object tracking
- Webcam video input
- Bounding boxes around detected objects
- Object labels displayed on screen

## Technologies Used

- Python
- OpenCV
- YOLOv8 (Ultralytics)

## Input

Live webcam video captured from the computer camera.

## Output

Detected objects displayed with:
- Bounding boxes
- Object labels
- Real-time tracking

## How It Works

1. The webcam captures live video.
2. YOLOv8 processes each frame.
3. Objects are detected and labeled.
4. Bounding boxes are drawn around detected objects.
5. Objects are tracked while they move.

## Note

The YOLOv8 model file (`yolov8n.pt`) is automatically downloaded by Ultralytics when the project is run for the first time.
