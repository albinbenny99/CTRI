import pandas as pd
import os
import re

def extract_info_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define patterns for extracting information
    patterns = {
        'CTRI Number': r"CTRI Number\s*(CTRI\/\d{4}\/\d{2}\/\d{6})\s*\[Registered on:\s*(\d{2}\/\d{2}\/\d{4})\]\s*Trial Registered\s*(\w+)",
        "Country of recruitment": r'Countries of Recruitment\s*(.*)',
        'Trial Type': r'Type of Trial\s*(.*)',
        "Phase of Trial": r'Phase of Trial\s*(.*)',
        "Recruitment Status in India": r'Recruitment Status of Trial \(India\)\s*(.*)',
        "Type of Study": r'Type of Study\s*(.*)',
    }
    data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            if key == "CTRI Number":
                data["CTRI Number"] = match.group(1).strip()
                data["Registered on Date"] = match.group(2).strip()
                data["Trial Registered"] = match.group(3).strip()
            else:
                data[key] = match.group(1).strip()
        else:
            data[key] = None  # If no match, set to None

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
output_file = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\done.xlsx'
df.to_excel(output_file, index=False)
