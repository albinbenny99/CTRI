import pandas as pd
import os
import re

# Define custom regular expression patterns and corresponding column names
custom_patterns = {
    r'CTRI/(\d{4}/\d{2}/\d{6})': 'CTRI Number',
    r'Registered on: (\d{2}/\d{2}/\d{4})': 'Registered on Date',
    r'Trial Registered (\w+)': 'Trial Registration Type',
    r'Type of Trial (\w+)': 'Type of Trial',
    r'Type of Study (\w+)': 'Type of Study',
    r'Phase of Trial (\w+)': 'Phase of Trial',
    r'Recruitment Status of Trial \(India\) (\w+)': 'Recruitment Status in India',
    r'Countries of Recruitment (\w+)': 'Countries of Recruitment'
}

# Initialize an empty DataFrame to store the extracted data
result_df = pd.DataFrame()

# Directory containing the CSV files
directory = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Left_over_CTRI_database_34 items'

# Iterate over each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)
        
        # Convert the DataFrame to JSON
        json_data = df.to_json(orient='records')
        
        # Initialize columns for each pattern
        for column_name in custom_patterns.values():
            df[column_name] = None
        
        # Extract data using each custom regular expression and store in respective columns
        for pattern, column_name in custom_patterns.items():
            df[column_name] = df[column_name].str.extract(pattern)
        
        # Concatenate the extracted data from this file to the result DataFrame
        result_df = pd.concat([result_df, df[list(custom_patterns.values())]], ignore_index=True)

        # Save the JSON data to a file for debugging
        with open(r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\output.json', 'w') as f:
            f.write(json_data)

# Save the final DataFrame to an Excel file
result_df.to_excel(r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\output9.xlsx', index=False)
