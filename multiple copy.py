import pandas as pd
import os
import re

# Function to extract information from a single file
def extract_info_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define patterns for extracting information
    patterns = {
        'CTRI Number': r"CTRI Number\s*(CTRI\/\d{4}\/\d{2}\/\d{6}\s*\[Registered on:\s*\d{2}\/\d{2}\/\d{4}\]\s*Trial Registered\s*\w+)",
        "Country of recruitment": r'Countries of Recruitment\s*(.*)',
        "Registered on Date": r"Registered on\s*:\s*([\d/]+)",
        "Trial Registration Type": r"Trial Registration Type\s*:\s*(.*)",
        'Trial Type': r'Type of Trial\s*->\s*(\w+)',
        "Phase of Trial": r"Phase of Trial\s*:\s*(.*)",
        "Recruitment Status in India": r"Recruitment Status in India\s*:\s*(.*)",
        "Type of Study": r"Type of Study\s*:\s*(.*)",
        'Study Design': r'Study Design\s*->\s*(.*)',
    }

    data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            data[key] = match.group(1).strip()

    return data

# Directory containing all CSV files
directory = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Left_over_CTRI_database_34 items'

# List to store extracted data from all files
all_data = []

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        data = extract_info_from_file(file_path)
        data["File"] = filename  # Include filename for reference
        all_data.append(data)

# Create a DataFrame from the extracted data
df = pd.DataFrame(all_data)

# Save the DataFrame to an Excel file
output_file = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\outpp.xlsx'
df.to_excel(output_file, index=False)
