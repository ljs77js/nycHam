import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. 
# Note 'None' in place of application token, and no username or password:
client = Socrata("data.cityofnewyork.us", None)

# Specify the dataset identifier
dataset_id = "76xm-jjuj"

# Specify the query
query = "borough = 'MANHATTAN'"

# Fetch the data
results = client.get(dataset_id, where=query)

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results)

# Select columns of interest
df = df[['zipcode', 'first_to_hosp_datetime', 'first_hosp_arrival_datetime', 'initial_call_type']]

# Save to a CSV file
df.to_csv('manhattan_data.csv', index=False)
