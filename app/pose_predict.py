from ultralytics import YOLO

# Load a model
model = YOLO('../checkpoints/pose/yolov8n-pose.pt')  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom model

# Predict with the model
results = model('../ultralytics/assets/bus.jpg')  # predict on an image
print(results)