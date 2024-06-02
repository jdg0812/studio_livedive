from math import radians, sin, asin, cos, sqrt

def calculateDistance(lat1, long1, lat2, long2):
    lat1=radians(lat1)
    long1=radians(long1)
    lat2=radians(lat2)
    long2=radians(long2)
    r = 6371 

    dlong = long2 - long1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlong/2)**2
    c = 2 * asin(sqrt(a))
    return(c * r)