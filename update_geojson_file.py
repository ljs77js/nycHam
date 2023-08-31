
import pandas as pd
import json

# Load the analyzed dataset
data_df = pd.read_csv('result_data.csv')

# Load the original NYC polygon GeoJSON file
with open('nyc-zip-code-tabulation-areas-polygons.geojson', 'r') as file:
    nyc_geo = json.load(file)

# Function to assign a color based on the most common incident type
def assign_color(incident_type):
    if incident_type == 'VIOLENT':
        return 'violet'
    elif incident_type == 'MIXED':
        return 'orange'
    else:  # 'NON-VIOLENT'
        return 'blue'

# Update the GeoJSON properties to include the most common incident type and its associated color
for feature in nyc_geo['features']:
    try:
        zipcode = int(feature['properties']['postalCode'])
        most_common_type = data_df[data_df['ZIPCODE'] == zipcode]['MOST_COMMON_TYPE'].values[0]
        color = assign_color(most_common_type)
        
        feature['properties']['MOST_COMMON_TYPE'] = most_common_type
        feature['properties']['COLOR'] = color
        
    except IndexError:
        # For zip codes not in our dataset
        feature['properties']['MOST_COMMON_TYPE'] = 'UNKNOWN'
        feature['properties']['COLOR'] = 'grey'

# Save the updated GeoJSON file
with open('updated_nyc_zipcodes.geojson', 'w') as outfile:
    json.dump(nyc_geo, outfile)

print("Updated GeoJSON file saved as 'updated_nyc_zipcodes.geojson'")
