#! /usr/bin/env python3
import os
import requests
import json

#call webserver api
def postFeedback(feedback):
    print(tempResult)
    response = requests.post("http://34.75.62.255/feedback/", json=feedback)
    print(response.status_code)

resultJson = {"title": "", "name": "", "date": "", "feedback": ""}
res_directory = "/data/feedback"
fb_files = os.listdir(res_directory)
print(fb_files)
script_directory = os.path.dirname(os.path.abspath(__file__))
for f in fb_files:
    tempResult = {}
    with open(res_directory + "/" + f, 'r') as fp:
        # To store lines
        for i, line in enumerate(fp):
            # read line 4 and 7
            if i == 0:
                tempResult["title"] = line.strip()
            elif i == 1:
                tempResult["name"] = line.strip()
            elif i == 2:
                tempResult["date"] = line.strip()
            elif i == 3:
                tempResult["feedback"] = line.strip()
    postFeedback(tempResult)