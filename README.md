# **Object-Detection**
## Overview
This project demonstrates how to use YOLO models to detect persons and caps in live video streams using a webcam. It employs a custom-trained YOLOv8 model for cap detection and a pre-trained YOLOv8 model for person detection.

## **Features**
* **Person Detection**: Uses a pre-trained YOLOv8 model to detect persons in video frames.
* **Cap Detection**: Utilizes a custom-trained YOLOv8 model to identify caps.
* **Real-Time Processing**: Processes live video from a webcam and annotates frames with detected objects.
* **Visualization**: Displays annotated frames with bounding boxes and labels for persons and caps.
  
## **Requirements**
* Python 3.x
* OpenCV
* Ultralytics YOLO library
  
## **Installation**
1. Clone the Repository:
   ```bash
    git clone https://github.com/Dishak0411/Object-Detection.git
    cd Object-Detction
 
2. Install Dependencies:
   ```bash
      pip install opencv-python ultralytics
   
3. Download Pre-trained Models:
* Download the pre-trained YOLOv8 model for person detection (yolov8n.pt) from Ultralytics.
* Ensure you have the custom-trained YOLOv8 model for cap detection (yolov8-custom-cap.pt). Place both models in the project directory.
 
## **Usage**
1. Run the Script:
   ```bash
     python detect.py
2. Control:
* The script will open a window displaying the live video feed from your webcam.
* Press 'q' to exit the application.
  
## **Code Explanation**
* detect.py: Main script that loads the YOLO models, captures video from the webcam, performs detection, and annotates frames.
  * Loads the custom YOLOv8 model (yolov8-custom-cap.pt) for cap detection.
  * Loads the pre-trained YOLOv8 model (yolov8n.pt) for person detection.
  * Captures video from the default webcam and processes each frame to detect and annotate persons and caps.

## **Challenges and Solutions**
* **Model Accuracy**: Ensured the custom-trained model could differentiate between caps and heads by expanding the dataset and refining annotations.
* **False Positives**: Implemented logic to filter out false positives by associating detected caps with persons based on bounding box regions.
* **Performance**: Optimized the processing pipeline for real-time performance.
  
## **Future Work**
* **Improvement of Detection Accuracy**: Continue refining the dataset and model to enhance detection accuracy.
* **Performance Optimization**: Further optimize for real-time performance and handle edge cases.
