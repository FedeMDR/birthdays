import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Assuming you have pandas and geopy installed and your DataFrame is loaded
# DataFrame df with a column 'address'
# geolocator = Nominatim(user_agent="translatecoordinates")
# print(geolocator)
df = pd.read_csv("/Users/simonedilorenzo/Downloads/New_York_Tourist_Locations.csv")

geolocator = Nominatim(user_agent="translatecoordinates", timeout=10)

def get_coordinates(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return get_coordinates(address)

# Apply the function to the 'address' column and create two new columns
df['latitude'], df['longitude'] = zip(*df['Address'].apply(get_coordinates))

# Now df has two new columns: 'latitude' and 'longitude'
print(df.head())



df.to_csv('filename.csv', index=False)