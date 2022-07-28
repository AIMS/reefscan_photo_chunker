import glob
from geo_distance import geo_distance
from box_photos import box_photos, lat_lon


one_metre = .000009
ten_metres =one_metre * 10
five_metres =one_metre * 5

photo_mask = "F:/Trip7696_ECORRAP5/field_data/2022_01_17_OCCH_FL1/processedData/*.jpg"
photos = glob.glob(photo_mask)
print (len(photos))

min_lat = 9999999
max_lat = -9999999
min_long = 9999999
max_long = -9999999
for photo in photos:
    data = lat_lon(photo)
    lat = data["Latitude"]
    long = data["Longitude"]
    if lat < min_lat:
        min_lat = lat
    if lat > max_lat:
        max_lat = lat
    if lat < min_long:
        min_long = long
    if lat > max_long:
        max_long = long

print (min_lat)
print (max_lat)
print (min_long)
print (max_long)

long_dist = geo_distance(min_long, min_lat, min_long, max_lat)
lat_dist = geo_distance(min_long, min_lat, max_long, min_lat)

print (lat_dist)
print (long_dist)

centre_lat = ((max_lat - min_lat) / 2) + min_lat
centre_long = ((max_long - min_long) / 2) + min_long

print (centre_lat)
print (centre_long)


box_photos("E:/metashape-test/OCCH_FL1/two_by_two", photos, centre_lat, centre_long, one_metre)
box_photos("E:/metashape-test/OCCH_FL1/ten_by_ten", photos, centre_lat, centre_long, five_metres)
box_photos("E:/metashape-test/OCCH_FL1/twenty_by_twenty", photos, centre_lat, centre_long, ten_metres)
