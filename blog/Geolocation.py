
import geopy
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from geopy import geocoders

def geolocation(zipcode):
    g = geocoders.GoogleV3(api_key='AIzaSyB7WTLJn0xu0C1Mkc118yUTehbB8jViv0Y')
    #inputAddress = 'Concordia SGW campus'
    location= g.geocode(zipcode,timeout=10)
    Lat_Long = (location.latitude, location.longitude)
    return(Lat_Long)

def Distance(Client_loc,Product_loc):
    g = geocoders.GoogleV3(api_key='AIzaSyC5c42RLoD-1Wfl9o8MIm0OhefZYWaOJE0')
    Radius = vincenty(Client_loc,Product_loc).meters
    geolocator = Nominatim()
   # postalcode = geolocator.reverse(Product_loc)
    return(Radius)

 #   print(location.latitude,location.longitude)
#print(location.raw)
#print(location.address)
    #newport_ri = (45.49577379999999, -73.5782521)
    #cleve_ri = (45.4953222, -73.5813589)
#print(vincenty(newport_ri, cleve_ri).meters)

#geolocator = Nominatim()
#location = geolocator.geocode("Montreal, H3H2J6")
#print(location.point)

#Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
#print((location.latitude, location.longitude))
#(40.7410861, -73.9896297241625)
#print(location.raw)
#{'place_id': '9167009604', 'type': 'attraction', ...}
