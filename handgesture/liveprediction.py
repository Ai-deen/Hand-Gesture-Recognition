import os
import random 
import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image, ImageOps
from PIL import Image as im


from keras.models import load_model
model = load_model(r'C:\Users\sreeja\Desktop\Projects\handgesture\model_B3.h5',compile=False)

from keras.models import load_model
model_base = load_model(r'C:\Users\sreeja\Desktop\Projects\handgesture\model_base.h5',compile=False)

map = { 0 :'one', 1 :  'peace' , 2 : 'thumbdown', 3 : 'four' , 4 : 'thumbup', 5 : 'three', 6 : 'yo' , 7 : 'ok' , 8 : 'five' }


# import cv2
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()

	# Display the resulting frame
	cv2.imshow('frame', frame)

	image = cv2.resize(frame, (100,100))
	images = []
	images.append(image)
	test = np.array(images)
	test
	y_pred = model.predict(test)
	print("EfficientNetB3 : ",map[np.argmax(y_pred)])

	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
