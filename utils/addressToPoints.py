from geopy.geocoders import Nominatim

def getPoint(place):
	locator = Nominatim(user_agent="myGeocoder")
	location = locator.geocode(place)
	print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
	return {"latitude":location.latitude, "longitude" : location.longitude}
