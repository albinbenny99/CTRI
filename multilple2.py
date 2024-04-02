import pandas as pd
import os
import re

# Function to extract information from a single file
def extract_info_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    print(f"File Path: {file_path}")

    # Print content with utf-8 encoding
    try:
        print(f"Content: {content}")
    except UnicodeEncodeError:
        print(f"Content: {content.encode('utf-8').decode('utf-8')}")

    # Define patterns for extracting information
    patterns = {
        'CTRI Number': r'CTRI Number\s*->\s*(CTRI\/\d{4}\/\d{2}\/\d{6})',
        "Country of recruitment": r"Country of recruitment\s*:\s*(.*)",
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
        else:
            print(f"No match found for pattern: {key}")

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
output_file = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\outpuu.xlsx'
df.to_excel(output_file, index=False)
