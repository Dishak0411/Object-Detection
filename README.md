# **Object-Detection**
## Overview
This project demonstrates how to use a custom-trained YOLOv8 model for multi-class object detection in live video streams from a webcam. The system is designed to detect and annotate persons and caps in real-time.

## **Features**
* **Multi-Class Detection**: Utilizes a custom-trained YOLOv8 model to detect multiple classes, specifically persons and caps.
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
   
3. Download YOLOv8 Model:
* Ensure you have the custom-trained YOLOv8 model (yolov8-custom.pt). Place this model file in the project directory.
 
## **Usage**
1. Run the Script:
   ```bash
     python detect.py
2. Control:
* The script will open a window displaying the live video feed from your webcam.
* Press 'q' to exit the application.
  
## **Code Explanation**
* detect.py: Main script that loads the YOLO models, captures video from the webcam, performs detection, and annotates frames.
  * **Loading the Model**: Loads the custom YOLOv8 model (yolov8-custom.pt) for multi-class detection.
  * **Detection and AnnotationCaptures**:
      * Detects persons and caps based on their class IDs.
      * Annotates the detected objects with bounding boxes and labels.
        
## **Detection Class IDs**
* Person: 3
* Cap: 1
Adjust these IDs based on how your custom model is trained if necessary.

## **Challenges and Solutions**
* **Model Accuracy**: Ensured the custom-trained model could differentiate between caps and heads by expanding the dataset and refining annotations.
* **False Positives**: Implemented logic to filter out false positives by associating detected caps with persons based on bounding box regions.
* **Performance**: Optimized the processing pipeline for real-time performance.
  
## **Future Work**
* **Improvement of Detection Accuracy**: Continue refining the dataset and model to enhance detection accuracy.
* **Performance Optimization**: Further optimize for real-time performance and handle edge cases.
