from flask import Flask,request

from geopy.geocoders import Nominatim

from utils.get_sat_image_02 import getSatImg
import json


# import cv2
import numpy as np
# import tensorflow as tf
# from keras.models import load_model


# import tensorflow


app = Flask(__name__)
 
@app.route('/')

def hello_world():

	return 'Hi'

@app.route('/getPrediction' ,methods = ['POST'] )

def getPrediction():
	# print(tf.__version__)
	request_data = json.loads(request.data)
	print(request_data['place'])
	res = getSatImg(request_data['place'])
	print(res)
	# model = load_model('droughtModel.h5')

	# model.compile(loss='binary_crossentropy',
    #           optimizer='rmsprop',
    #           metrics=['accuracy'])

	# img = cv2.imread(sat_image)
	# img = cv2.resize(img,(320,240))
	# img = np.reshape(img,[1,320,240,3])

	# classes = model.predict_classes(img)

	# print(classes)
	# saved_model = load_model('droughtModel.h5')
	# print("**")
	# prediction = model.predict(sat_image)

	# print(prediction)
	# print(hf['model_weights'].values())
	# print(sat_image)
	return res


if __name__ == '__main__':
    
	app.run()
