from flask import Flask,request

from geopy.geocoders import Nominatim

from utils.get_sat_image_02 import getSatImg
import json
from tensorflow.keras.models import load_model


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
	model = load_model('droughtModel.h5')
	model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
	print(model.summary())
 
	return res



@app.route('/healthz')
def healthz():
    return ''


if __name__ == '__main__':
    
	app.run(debug=False)
