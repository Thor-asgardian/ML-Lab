import pandas as pd
from pandas_profiling import ProfileReport

# Specify the correct file path to the CSV file
df = pd.read_csv('housing.csv')

print(df)

# Generate the pandas profiling report
profile = ProfileReport(df,minimal=True)
profile.to_file(output_file="housing.html")
