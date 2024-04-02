import pandas as pd
import os
import re
import pdfplumber

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

# Directory containing the PDF files
directory = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Left_over_CTRI_database_34 items'

# Initialize an empty DataFrame to store the extracted data
result_df = pd.DataFrame()

# Iterate over each PDF file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        filepath = os.path.join(directory, filename)
        
        # Open the PDF file
        with pdfplumber.open(filepath) as pdf:
            # Initialize an empty string to store the extracted text
            extracted_text = ''
            # Extract text from each page of the PDF
            for page in pdf.pages:
                extracted_text += page.extract_text()
        
        # Initialize an empty DataFrame to store the extracted data for this file
        df = pd.DataFrame(columns=custom_patterns.values())
        
        # Extract data using each custom regular expression and store in respective columns
        for pattern, column_name in custom_patterns.items():
            # Search for the pattern in the extracted text
            matches = re.findall(pattern, extracted_text)
            # Assign the matched value to the corresponding column
            if matches:
                df[column_name] = matches[0]  # Assuming only one match is needed
        
        # Concatenate the extracted data from this file to the result DataFrame
        result_df = pd.concat([result_df, df], ignore_index=True)

# Save the final DataFrame to an Excel file
result_df.to_excel(r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\output90.xlsx', index=False)
