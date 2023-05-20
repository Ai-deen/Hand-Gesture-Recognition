import os
import subprocess
import random 
import cv2
import sys
import serial
import time 
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image, ImageOps
from PIL import Image as im


from keras.models import load_model
model = load_model(r'C:\Users\sreeja\Desktop\handgesture\model_B3.h5',compile=False)

from keras.models import load_model
model_base = load_model(r'C:\Users\sreeja\Desktop\handgesture\model_base.h5',compile=False)

map = { 0 :'one', 1 :  'peace' , 2 : 'thumbdown', 3 : 'four' , 4 : 'thumbup', 5 : 'three', 6 : 'yo' , 7 : 'ok' , 8 : 'five' }


import cv2

# define a video capture object
subprocess.Popen('C:\\Infineon\\Tools\Radar GUI\\2.8.2.202205190911\\radargui.exe')
time.sleep(40)

vid = cv2.VideoCapture(0)

subprocess.call("TASKKILL /F /IM radargui.exe", shell=True)

# # print(path)
# path = r"C:\Users\sreeja\Desktop\radar dataset\Distance2Go_record_20230425-173758.trg"
# with open(path) as f:
#     contents = f.readlines()

# contents

#print(contents)
#type(contents)
# contents[0][0:len(contents[0])-3]

# a = []
# for i in contents:
#     i = i[1:len(i)-3]
#     a.append(i)
# #print(a)

# path = r"C:\Users\sreeja\Desktop\radar dataset\Distance2Go_record_20230425-173758.trg"
# with open(path) as f:
#     contents = f.readlines()
    
# a = []
# for i in contents:
#     i = i[:len(i)-4]
#     a.append(i)
    
# #print(a)

# for i in a:
#     if i!='':
#         li = list(i.split(","))
#         print(li[1],li[2])


# path = r"C:\Users\sreeja\Desktop\radar dataset\Distance2Go_record_20230425-173758.trg"

import sys
folder_path ="C:\\Users\\sreeja\\Desktop\\radar dataset"
files= os.listdir(folder_path)

path= os.path.join(folder_path,files[1]);

with open(path) as f:
    contents = f.readlines()
flag=0   
for i in contents:
    i = i[1:len(i)-3]
    if i!='':
        li = list(i.split(","))
        strength = float(li[1])
        distance = float(li[2])
        if strength>100 and distance< 80:
            print('yes')
            flag=1
        # else:
        #     sys.exit()

while(flag==1):
	
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    time.sleep(8)

    image = cv2.resize(frame, (100,100))
    images = []
    images.append(image)
    test = np.array(images)
    y_pred = model.predict(test)

    print("EfficientNetB3 : ",map[np.argmax(y_pred)])

    k = np.argmax(y_pred)
    # print(k)
    break
    # print(k)
    # if True:
    #     break
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    # 	break
	# k=0,1,2,3,4,5,6,7
    
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	

# After the loop release the cap object
vid.release()

print(k)
ser = serial.Serial('COM12', 9600, timeout=1)
time.sleep(2)

pin_number= (k%4)+4
ser.write(str(pin_number).encode())

ser.close()
exit()

# Destroy all the windows
cv2.destroyAllWindows()