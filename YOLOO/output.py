import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from collections import OrderedDict

yolo = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg") #using yolov4 config files & Weights
classes = []
tot={}
csv_column='filename' #initializing columns name for csv
with open("D:/YOLOO/coco.names",'r') as file:
    classes = [line.strip() for line in file.readlines()]
    for i in classes:
        csv_column=csv_column+','+i 
        tot[i]=0
    csv_column=csv_column+','+'total_count'

print(csv_column)

# #writing column names to csv
# bill=open('data.csv','w')
# bill.write(csv_column)
# bill.close()