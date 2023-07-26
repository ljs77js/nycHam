import pandas as pd

# Load the CSV file
df = pd.read_csv('manhattan_data.csv', low_memory=False)

# Filter out the columns you're interested in and create a copy
df_filtered = df[['ZIPCODE', 'FIRST_HOSP_ARRIVAL_DATETIME', 'INITIAL_CALL_TYPE', 'FIRST_TO_HOSP_DATETIME']].copy()

# Convert dates from string to datetime
df_filtered['FIRST_HOSP_ARRIVAL_DATETIME'] = pd.to_datetime(df_filtered['FIRST_HOSP_ARRIVAL_DATETIME'], format='%Y %b %d %I:%M:%S %p')
df_filtered['FIRST_TO_HOSP_DATETIME'] = pd.to_datetime(df_filtered['FIRST_TO_HOSP_DATETIME'], format='%Y %b %d %I:%M:%S %p')

# Compute the time it took to get to the hospital
df_filtered['TIME_TO_HOSPITAL'] = df_filtered['FIRST_TO_HOSP_DATETIME'] - df_filtered['FIRST_HOSP_ARRIVAL_DATETIME']

# Write the filtered DataFrame to a new CSV file
df_filtered.to_csv('manhattan_sorted_data.csv', index=False)
