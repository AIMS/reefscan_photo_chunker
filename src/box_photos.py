import piexif
from geo_distance import geo_distance
import shutil


def box_photos(out_dir, photos, centre_lat, centre_long, size):
    min_lat = centre_lat - size
    max_lat = centre_lat + size

    min_long = centre_long - size
    max_long = centre_long + size

    print(min_lat)
    print(max_lat)
    print(min_long)
    print(max_long)

    long_dist = geo_distance(min_long, min_lat, min_long, max_lat)
    lat_dist = geo_distance(min_long, min_lat, max_long, min_lat)

    print(lat_dist)
    print(long_dist)

    for photo in photos:
        data = lat_lon(photo)
        lat = data["Latitude"]
        long = data["Longitude"]
        if min_lat < lat < max_lat and min_long < long < max_long:
            shutil.copy(photo, out_dir)


def lat_lon(photo):
    exif_dict = piexif.load(photo)
    gps = exif_dict['GPS']
    lat_dir = gps[piexif.GPSIFD.GPSLatitudeRef]
    lat = dec_deg(gps[piexif.GPSIFD.GPSLatitude], lat_dir)
    lon_dir = gps[piexif.GPSIFD.GPSLongitudeRef]
    lon = dec_deg(gps[piexif.GPSIFD.GPSLongitude], lon_dir)

    return {"Latitude": lat, "Longitude": lon}

def dec_deg(array, dir):

    number = (array[0][0] / array[0][1]) + (array[1][0] / array[1][1] / 60) + (array[2][0] / array[2][1] / 3600)
    if dir == 'S' or dir == 'W':
        number = number*-1
    return number
