import pandas as pd

def process_data(input_file, output_file, threshold=100):
    # Read the CSV file
    df = pd.read_csv(input_file, low_memory=False)
    
    # Drop rows where ZIPCODE is NaN and then convert to integer
    df = df.dropna(subset=['ZIPCODE'])
    df['ZIPCODE'] = df['ZIPCODE'].astype(str).str.split('.').str[0]  # Convert float to int string
    df = df[df['ZIPCODE'].str.isnumeric()]  # Keep only numeric ZIP codes
    df['ZIPCODE'] = df['ZIPCODE'].astype(int)
    
    # Identify the top 10 most common call types
    top_10_call_types = df['INITIAL_CALL_TYPE'].value_counts().head(10).index.tolist()

    # Include STAB and SHOT
    selected_call_types = set(top_10_call_types + ['STAB', 'SHOT'])

    # Filter dataframe to only include selected call types
    df = df[df['INITIAL_CALL_TYPE'].isin(selected_call_types)]
    
    # Group by ZIPCODE and INITIAL_CALL_TYPE and count the occurrences
    grouped = df.groupby(['ZIPCODE', 'INITIAL_CALL_TYPE']).size().unstack().fillna(0).astype(int)
    
    # Filter out ZIP codes with total counts below the threshold
    grouped = grouped[grouped.sum(axis=1) >= threshold]
    
    # Find the most common call type per ZIPCODE
    grouped['MOST_COMMON_TYPE'] = grouped.idxmax(axis=1)
    
    # Reset index for the dataframe to have ZIPCODE as a column
    grouped.reset_index(inplace=True)
    
    # Save the results to the output CSV file
    grouped.to_csv(output_file, index=False)

# Using the function
process_data('manhattan_data.csv', 'result_data.csv')
