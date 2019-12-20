import json
import os
import shutil

with open("clean.json") as json_file:
    data = json.load(json_file)
    for i in range(len(data)):
        dirName = data[i]["image"].split("/")[0]
        s = os.path.join(os.getcwd()+"/../lfw",dirName)
        d = os.path.join(os.getcwd()+"/../datasetFace",dirName)
        if os.path.isdir(s):
            shutil.copytree(s,d,False,None)
