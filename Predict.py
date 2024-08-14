import os
import json
import cv2
from Model import detect_faces_retinaface  # Ensure the import matches the filename

METADATA_FILE = 'metadata.json'

def save_metadata(image_path, num_faces):
    """
    Save face detection metadata to a JSON file.
    
    Args:
        image_path (str): Path to the processed image.
        num_faces (int): Number of faces detected.
    """
    metadata = {
        "image_path": image_path,
        "num_faces": num_faces
    }
    
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'r') as file:
            all_metadata = json.load(file)
    else:
        all_metadata = []
    
    all_metadata.append(metadata)
    
    with open(METADATA_FILE, 'w') as file:
        json.dump(all_metadata, file, indent=4)

def process_image(input_image_path, output_folder):
    """
    Process an image for face detection and save results.
    
    Args:
        input_image_path (str): Path to the input image.
        output_folder (str): Directory to save the processed image.
    
    Returns:
        tuple: Path to the saved image and number of detected faces.
    """
    output_image, detected_faces = detect_faces_retinaface(input_image_path)
    
    output_image_path = os.path.join(output_folder, os.path.basename(input_image_path))
    cv2.imwrite(output_image_path, output_image)
    
    save_metadata(output_image_path, detected_faces)
    
    return output_image_path, detected_faces
