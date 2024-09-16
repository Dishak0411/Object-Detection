import cv2
from ultralytics import YOLO

# Load the custom YOLOv8 model for multi-class detection
model = YOLO("yolov8-custom.pt")

# Using captured video
# cap = cv2.VideoCapture(r"C:\Users\disha\OneDrive\Desktop\Object_Detection\SampleVideo.mp4")

# Open the webcam for live video stream
cap = cv2.VideoCapture(0)

# Define class IDs for the objects you want to track
PERSON_CLASS_ID = 3
CAP_CLASS_ID = 1

# Loop through the video frames
while cap.isOpened():
    success, frame = cap.read()

    if success:
        # Run detection using the trained YOLOv8 model
        results = model.track(frame, persist=True)

        # Extract bounding boxes for detected objects
        person_boxes = []
        cap_boxes = []
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                confidence = box.conf[0]

                # if confidence > CONF_THRESHOLD:
                if class_id == PERSON_CLASS_ID:
                    person_boxes.append(box)
                elif class_id == CAP_CLASS_ID:
                    cap_boxes.append(box)

        # Annotate the frame with detection results
        for box in person_boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # Draw the bounding box (Person) in green
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, "Person", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        for box in cap_boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # Draw the bounding box (Cap) in blue
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, "Cap", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Display the combined annotated frame
        cv2.imshow("YOLOv8 Tracking (Persons and Caps)", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
