## Objective:
To analyze EMS dispatch data for Manhattan and identify the most common call types per ZIP code, while focusing on the top 10 most common call types and specific crucial types (`STAB` and `SHOT`). The goal is to create a CSV file that provides insights into the predominant call types for each ZIP code, and to filter out ZIP codes that don't have a statistically significant number of calls.

## Steps:

1. **Data Extraction and Transformation**:
   - We began by creating a `DataFilter` class to extract and preprocess the data. 
   - Loaded the CSV file and parsed date columns.
   - Filtered the dataset for incidents from Manhattan.
   - Selected relevant columns: `ZIPCODE`, `FIRST_TO_HOSP_DATETIME`, `FIRST_HOSP_ARRIVAL_DATETIME`, and `INITIAL_CALL_TYPE`.
   - Converted date columns to a standardized format.
   - Saved the preprocessed data to a new CSV file.

2. **Data Analysis**:
   - We then created a function `process_data` to analyze the preprocessed data.
   - Read the preprocessed CSV file.
   - Cleaned the `ZIPCODE` data by converting floats to integers and filtering out non-numeric entries.
   - Identified the top 10 most common call types, and included `STAB` and `SHOT` for their significance.
   - Filtered the dataset to only include these selected call types.
   - Grouped the data by `ZIPCODE` and `INITIAL_CALL_TYPE` to count occurrences.
   - Identified the most common call type for each ZIP code.
   - Filtered out ZIP codes with a total count of incidents below a specified threshold (e.g., 100) to focus on statistically meaningful data.
   - Saved the analyzed data to a new CSV file.

3. **Challenges and Solutions**:
   - We encountered an issue with ZIP codes being recorded in two formats (`10000` and `10000.0`). We resolved this by cleaning the `ZIPCODE` column and ensuring consistency.
   - The initial data included many unique call types. To make the analysis more meaningful, we focused on the top 10 most common call types and specifically included `STAB` and `SHOT`.
   - Some ZIP codes had very few incidents, which might not be statistically meaningful. To address this, we added a threshold filter to exclude ZIP codes with a total count of incidents below a specified number.

## Result:
We successfully produced a CSV file that displays, for each ZIP code:
   - Counts for the top 10 call types and for `STAB` and `SHOT`.
   - The most common call type.
ZIP codes with insufficient data (below the threshold) were excluded to ensure statistical significance.

This analysis provides insights into the predominant EMS call types for different parts of Manhattan, allowing for better resource allocation and understanding of the most prevalent emergencies in each area.