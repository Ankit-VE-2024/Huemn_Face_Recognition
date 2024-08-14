# Model.py

import cv2
from retinaface import RetinaFace

def detect_faces_retinaface(image_path):
    """
    Detect faces in an image using RetinaFace and draw bounding boxes.
    
    Args:
        image_path (str): Path to the input image.
    
    Returns:
        tuple: Image with bounding boxes and number of detected faces.
    """
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Could not load image at path: {image_path}")
    
    # Perform face detection using RetinaFace
    detections = RetinaFace.detect_faces(image)
    
    detected_faces = 0
    
    # Draw bounding boxes
    for key in detections:
        detection = detections[key]
        facial_area = detection["facial_area"]
        x, y, x2, y2 = facial_area
        confidence = detection["score"]
        
        # Draw the bounding box
        cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)
        detected_faces += 1
    
    return image, detected_faces
