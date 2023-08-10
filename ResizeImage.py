#!/usr/bin/env python3
from PIL import Image
import os

# Path to the folder containing the images
images_folder_path = "images"

# Create the output folder in the same directory as the script
script_directory = os.path.dirname(os.path.abspath(__file__))
output_folder = "/opt/icons"
os.makedirs(output_folder, exist_ok=True)

# Degree of rotation
rotation_degree = 90  # Change this to your desired degree

# Get a list of all image files in the folder
image_files = [file for file in os.listdir(images_folder_path)]

# Iterate through each TIFF image file and perform rotation
for image_file in image_files:
    image_path = os.path.join(images_folder_path, image_file)

    try:
        # Open the TIFF image using PIL
        img = Image.open(image_path)

        # Convert the image to the "RGB" mode before rotating
        img = img.convert("RGB")

        # Rotate the image by the specified degree; resize it to 128/128
        rotated_img = img.rotate(rotation_degree, expand=True).resize((128,128))

        # Save the rotated image as JPEG in the output folder
        rotated_image_path = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}.jpeg")
        rotated_img.save(rotated_image_path, "JPEG")

        print(f"Rotated {image_file} by {rotation_degree} degrees and saved as {rotated_image_path}")
    except Exception as e:
        print(f"Error processing {image_file}: {e}")

print("Rotation process completed.")
