import pandas as pd

class DataFilter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def filter_by_borough(self, borough_name):
        self.df = self.df.loc[self.df['BOROUGH'] == borough_name]

    def save(self, output_file):
        self.df.to_csv(output_file, index=False)

# Using the class
data_filter = DataFilter('./EMS/EMS_Incident_Dispatch_Data.csv')
data_filter.filter_by_borough('MANHATTAN')
data_filter.save('manhattan_data.csv')
