import pandas as pd
import geopandas as gpd
import ast

# Load the dataset
data_df = pd.read_csv('adjusted_data.csv')

# Load the GeoJSON file using geopandas
gdf = gpd.read_file('nyc-zip-code-tabulation-areas-polygons.geojson')

# Extract the postal code and its centroid
gdf['CENTROID'] = gdf['geometry'].centroid.to_crs(epsg=4326)

# Convert the GeoDataFrame to a DataFrame for easier merging
centroid_df = gdf[['postalCode', 'CENTROID']]

# Merge the dataframes on ZIP code
data_df["ZIPCODE"] = data_df["ZIPCODE"].astype(str)
merged_df = pd.merge(data_df, centroid_df, left_on='ZIPCODE', right_on='postalCode', how='left')

# Convert the CENTROID column to a tuple of (latitude, longitude)
merged_df['CENTROID'] = merged_df['CENTROID'].apply(lambda x: (x.y, x.x) if pd.notnull(x) else None)

# Drop the redundant postalCode column
merged_df.drop('postalCode', axis=1, inplace=True)

# Save the merged dataframe
merged_df.to_csv('adjusted_data_with_centroid.csv', index=False)
