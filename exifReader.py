import exifread

def toDegress(val):
    if val == 0:
        return "the image not contains Location"
    d = float(val.values[0].num) / float(val.values[0].den)
    m = float(val.values[1].num) / float(val.values[1].den)
    s = float(val.values[2].num) / float(val.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)

def process_img(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f)

    if len(tags) == 0:
        return "error can't see metadata"

    lat = toDegress(tags.get('GPS GPSLatitude', '0'))
    lon = toDegress(tags.get('GPS GPSLongitude', '0'))
    lat_ref = tags.get('GPS GPSLatitudeRef')
    lon_ref = tags.get('GPS GPSLongtitudeRef')

    if lat_ref != 'N':
        lat = -lat
    if lon_ref != 'E':
        lon = -lon

    info = {
        'Image DateTime': tags.get('Image DateTime', '0'),
        'GPS Latitude': lat,
        'GPS Longitude': lon
    }
    return info

info = process_img('image here.jpg')
print (info)