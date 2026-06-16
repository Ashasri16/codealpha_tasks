from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:

    # Read frame
    ret, frame = cap.read()

    if not ret:
        break

    # Detect and track objects
    results = model.track(
        frame,
        persist=True
    )

    # Draw boxes and labels
    annotated_frame = results[0].plot()

    # Display output
    cv2.imshow(
        "Object Detection and Tracking",
        annotated_frame
    )

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()