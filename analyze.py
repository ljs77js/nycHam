import pandas as pd

# Load the Excel file
df = pd.read_excel('your_file.xlsx', engine='openpyxl')

# Sort the data based on category
df = df.sort_values(by='your_category')

# Filter out the columns you're interested in
df_filtered = df[['ZIPCODE', 'INCIDENT_DATETIME', 'INITIAL_CALL_TYPE', 'FIRST_TO_HOSP_DATETIME']]

# Convert dates from string to datetime
df_filtered['INCIDENT_DATETIME'] = pd.to_datetime(df_filtered['INCIDENT_DATETIME'])
df_filtered['FIRST_TO_HOSP_DATETIME'] = pd.to_datetime(df_filtered['FIRST_TO_HOSP_DATETIME'])

# Compute the time it took to get to the hospital
df_filtered['TIME_TO_HOSPITAL'] = df_filtered['FIRST_TO_HOSP_DATETIME'] - df_filtered['INCIDENT_DATETIME']

# Write the filtered and sorted DataFrame to a new Excel file
df_filtered.to_excel('sorted_data.xlsx', index=False, engine='openpyxl')
