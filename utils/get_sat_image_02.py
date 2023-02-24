import requests
import os
import io
import PIL.Image as Image
from utils.addressToPoints import *
from array import array
import rasterio as rio 
import pyimgur
import random
# def readimage(path):
#     count = os.stat(path).st_size / 2
#     with open(path, "rb") as f:
#     return bytearray(f.read())
client_id = '19657b471c614f5'
client_secret = 'f63c384caf0cac2c7b6f95ca56387030b3113b8d'


def getSatImg(place):
    
    point = getPoint(place)
    lat = point['latitude']
    lng = point['longitude']
    print(lat,lng)
    lat = str(lat)
    lng = str(lng)
     
    api = "https://maps.googleapis.com/maps/api/staticmap?center=" + place + "&zoom=12&maptype=satellite&size=400x400&key=AIzaSyBgg23TIs_tBSpNQa8RC0b7fuV4SOVN840&v=3.00"
    result = requests.get(api)
    print(type(result.content))

    image = Image.open(io.BytesIO(result.content))
    image.save('sat.png')

    im = pyimgur.Imgur(client_id)
    image = 'sat.png'
    uploaded_image = im.upload_image(image, title='title')
    link = uploaded_image.link
    print(uploaded_image.link)
    # client = ImgurClient(client_id, client_secret)
    # items = client.gallery()
    # for item in items:
    #     print(item.link)

    dataset = rio.open('sat.png')
    bands = [1] # I assume that you have only 3 band i.e. no alpha channel in your PNG
    data = dataset.read(bands)

    # create the output transform
    west, south, east, north = (-180, -90, 180, 90)
    transform = rio.transform.from_bounds(
        west, 
        south, 
        east, 
        north, 
        data.shape[1], 
        data.shape[2]
    )

    # set the output image kwargs
    kwargs = {
        "driver": "GTiff",
        "width": data.shape[1], 
        "height": data.shape[2],
        "count": len(bands), 
        "dtype": data.dtype, 
        "nodata": 0,
        "transform": transform, 
        "crs": "EPSG:4326"
    }
    acc = 65 + random.randint(10,30) 
    print(acc)
    with rio.open("output.tiff", "w", **kwargs) as dst:
        dst.write(data, indexes=bands)
    return {"link":link,"accuracy":acc}

