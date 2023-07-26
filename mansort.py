import pandas as pd

class DataFilter:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path, low_memory=False, parse_dates=['FIRST_TO_HOSP_DATETIME', 'FIRST_HOSP_ARRIVAL_DATETIME'])

    def filter_by_borough(self, borough_name):
        self.df = self.df.loc[self.df['BOROUGH'] == borough_name]

    def select_columns(self, columns):
        self.df = self.df[columns]

    def convert_datetime_format(self):
        for column in ['FIRST_TO_HOSP_DATETIME', 'FIRST_HOSP_ARRIVAL_DATETIME']:
            self.df[column] = self.df[column].dt.strftime('%Y-%m-%d %H:%M:%S')

    def save(self, output_file):
        # Save only the first 100 rows
        self.df.head(100).to_csv(output_file, index=False)

# Using the class
data_filter = DataFilter('./EMS_Incident_Dispatch_Data.csv')
data_filter.filter_by_borough('MANHATTAN')
data_filter.select_columns(['ZIPCODE', 'FIRST_TO_HOSP_DATETIME', 'FIRST_HOSP_ARRIVAL_DATETIME', 'INITIAL_CALL_TYPE'])
data_filter.convert_datetime_format()
data_filter.save('manhattan_data.csv')
