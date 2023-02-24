import requests
import os
import io
import PIL.Image as Image
from utils.addressToPoints import *
from array import array

# def readimage(path):
#     count = os.stat(path).st_size / 2
#     with open(path, "rb") as f:
#     return bytearray(f.read())

def getSatImg(place):
    
    point = getPoint(place)
    lat = point['latitude']
    lng = point['longitude']
    print(lat,lng)
    api = 'https://maps.googleapis.com/maps/api/staticmap?center={lat}%2c%20-{lng}&zoom=12&maptype=satellite&size=400x400&key=AIzaSyBgg23TIs_tBSpNQa8RC0b7fuV4SOVN840'
    result = requests.get(api)
    print(type(result.content))

    image = Image.open(io.BytesIO(result.content))
    image.save('sat.png')
    return image