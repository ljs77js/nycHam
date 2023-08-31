import pandas as pd
import folium

# Load data
data_df = pd.read_csv('adjusted_data.csv')

# Define the function to assign color based on the most common incident type
def assign_color(incident_type):
    if incident_type == "VIOLENT":
        return "violet"
    elif incident_type == "MIXED":
        return "orange"
    else:
        return "blue"

# Define the function to assign marker color based on the most common incident type
def assign_marker_color(incident_type):
    if incident_type == "VIOLENT":
        return "purple"
    elif incident_type == "MIXED":
        return "darkorange"
    else:
        return "blue"

# Create a base map
m = folium.Map(location=[40.730610, -73.935242], zoom_start=11)

# Overlay the polygons with colors based on classification and tooltips for zip code
for _, row in data_df.iterrows():
    centroid = row['CENTROID']
    if centroid and isinstance(centroid, list) and len(centroid) == 2:
        folium.Marker(
            location=centroid[::-1],  # reverse the order for folium
            tooltip=f"ZIP Code: {row['ZIPCODE']}, Most Common Incident: {row['MOST_COMMON_TYPE']}",
            icon=folium.Icon(color=assign_marker_color(row['MOST_COMMON_TYPE']), icon="info-sign")
        ).add_to(m)

# Save the map to an HTML file
m.save('nyc_updated_incident_map.html')
