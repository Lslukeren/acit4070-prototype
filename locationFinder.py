from geopy.geocoders import Nominatim
from geopy import distance

def findDistance(departure, destination):
    geolocator = Nominatim(user_agent="ACIT4070")

    departureLocation = departure
    destinationLocation = destination

    location1 = geolocator.geocode(departureLocation)
    location2 = geolocator.geocode(destinationLocation)
    try:
        loc1_lat = location1.latitude
        loc1_long = location1.longitude
        fromLoc = (loc1_lat, loc1_long)

        loc2_lat = location2.latitude
        loc2_long = location2.longitude
        toLoc = (loc2_lat, loc2_long)

        d = round(float(distance.distance(fromLoc, toLoc).km), 2)
        return d
    except AttributeError:
        pass
    #fromLoc = (loc1_lat, loc1_long)
    #toLoc = (loc2_lat, loc2_long)


    # Just does a really simple calculation with airspace as distance

    #print("Rip")


