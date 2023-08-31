
import pandas as pd
import folium
import geopandas as gpd

# Load the adjusted dataset with centroid
data_df = pd.read_csv('adjusted_data_with_centroid.csv')

# Load the NYC ZIP code GeoJSON
nyc_geo = gpd.read_file('nyc-zip-code-tabulation-areas-polygons.geojson')

# Define color assignment function
def assign_color(incident_type):
    if incident_type == 'Violent':
        return 'red'
    elif incident_type == 'Mixed':
        return 'orange'
    else:
        return 'green'

# Modify the style function to handle zip codes not in our dataset
def style_function(feature):
    try:
        most_common_type = data_df[data_df['ZIPCODE'] == int(feature['properties']['postalCode'])]['MOST_COMMON_TYPE'].values[0]
        color = assign_color(most_common_type)
    except IndexError:
        color = 'grey'  # default color for zip codes not in our dataset
    return {
        'fillColor': color,
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.7
    }

# Create a new map with colored polygons
m_colored = folium.Map(location=[40.730610, -73.935242], zoom_start=11)

# Overlay the polygons with colors based on classification and tooltips for zip code
folium.GeoJson(
    nyc_geo,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=['postalCode', 'borough'], labels=True, sticky=False)
).add_to(m_colored)

# Save map to HTML
m_colored.save('nyc_incident_map.html')

