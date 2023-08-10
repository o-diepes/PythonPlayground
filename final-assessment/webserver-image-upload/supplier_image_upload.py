#!/usr/bin/env python3
import requests
import os

def upload_image(path):
  url = "http://34.125.197.103/upload/"
  with open(path, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
      if r.ok:
        print("Upload successful!")
      else:
        print("An error occured: {}".format(r.status_code))
images_folder_path = "supplier-data/images"

# Create the output folder in the same directory as the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Get a list of all image files in the folder
image_files = [file for file in os.listdir(images_folder_path) if file.endswith(".jpeg")]

# Iterate through each TIFF image file and perform rotation
for image_file in image_files:
    image_path = os.path.join(images_folder_path, image_file)
    upload_image(script_directory + "/" + image_path)
