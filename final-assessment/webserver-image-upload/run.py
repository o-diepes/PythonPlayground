#! /usr/bin/env python3
import os
import requests

#call webserver api
def postFruit(fruit):
    response = requests.post("http://34.125.197.103/fruits/", json=fruit)
    print(response.status_code)

res_directory = "supplier-data/descriptions"
fb_files = os.listdir(res_directory)
print(fb_files)
script_directory = os.path.dirname(os.path.abspath(__file__))
for f in fb_files:
    tempResult = {}
    with open(res_directory + "/" + f, 'r') as fp:
        # To store lines
        for i, line in enumerate(fp):
            # read line 1-3
            if i == 0:
                tempResult["name"] = line.strip()
            elif i == 1:
                tempResult["weight"] = int(line.strip().split(" ")[0])
            elif i == 2:
                tempResult["description"] = line.strip()
            tempResult["image_name"] = f.replace(".txt", ".jpeg")
    postFruit(tempResult)
