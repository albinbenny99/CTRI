import pandas as pd
import re

# Read the CSV file into a pandas DataFrame


df = pd.read_csv(r"C:\Users\Anasiya\Downloads\ALL_Records_CTRI\CTRI_Database_part2_39,970 items\MjA0MDA.csv", header=None)

# Initialize variables to store extracted data
ctri_number = ""
registered_on = ""
trial_type = ""
study_design = ""
public_title = ""
scientific_title = ""
primary_investigator_name = ""
primary_investigator_affiliation = ""
primary_investigator_phone = ""
primary_investigator_email = ""
sponsor_name = ""
sponsor_address = ""
sites_of_study = ""

# Regular expressions patterns for extracting data
patterns = {
    'CTRI Number': r'CTRI Number\s*->\s*(CTRI\/\d{4}\/\d{2}\/\d{6})',
    'Registered On': r'Registered on:\s*(\d{2}\/\d{2}\/\d{4})',
    'Trial Type': r'Type of Trial\s*->\s*(\w+)',
    'Study Design': r'Study Design\s*->\s*(.*)',
    'Public Title': r'Public Title of Study\s*->\s*(.*)',
    'Scientific Title': r'Scientific Title of Study\s*->\s*(.*)',
    'Primary Investigator Name': r'Name\s*->\s*(.*)',
    'Primary Investigator Affiliation': r'Affiliation\s*->\s*(.*)',
    'Primary Investigator Phone': r'Phone\s*->\s*(.*)',
    'Primary Investigator Email': r'Email\s*->\s*(.*)',
    'Sponsor Name': r'Name\s*->\s*(.*)',
    'Sponsor Address': r'Address\s*->\s*(.*)',
    'Sites of Study': r'No of Sites\s*->\s*(.*)'
}

# Iterate over each row in the DataFrame and extract data
for index, row in df.iterrows():
    if isinstance(row[0], float):
        continue  # Skip this row if the first element is a float
    row_value = str(row[0])
    for key, pattern in patterns.items():
        match = re.search(pattern, row_value)
        if match:
            if key == 'CTRI Number':
                ctri_number = match.group(1)
            elif key == 'Registered On':
                registered_on = match.group(1)
            elif key == 'Trial Type':
                trial_type = match.group(1)
            elif key == 'Study Design':
                study_design = match.group(1)
            elif key == 'Public Title':
                public_title = match.group(1)
            elif key == 'Scientific Title':
                scientific_title = match.group(1)
            elif key == 'Primary Investigator Name':
                primary_investigator_name = match.group(1)
            elif key == 'Primary Investigator Affiliation':
                primary_investigator_affiliation = match.group(1)
            elif key == 'Primary Investigator Phone':
                primary_investigator_phone = match.group(1)
            elif key == 'Primary Investigator Email':
                primary_investigator_email = match.group(1)
            elif key == 'Sponsor Name':
                sponsor_name = match.group(1)
            elif key == 'Sponsor Address':
                sponsor_address = match.group(1)
            elif key == 'Sites of Study':
                sites_of_study = match.group(1)

# Create a new DataFrame or Excel sheet with the extracted data
# For now, let's print the extracted data
print(f"CTRI Number: {ctri_number}")
print(f"Registered On: {registered_on}")
print(f"Trial Type: {trial_type}")
print(f"Study Design: {study_design}")
print(f"Public Title: {public_title}")
print(f"Scientific Title: {scientific_title}")
print(f"Primary Investigator Name: {primary_investigator_name}")
print(f"Primary Investigator Affiliation: {primary_investigator_affiliation}")
print(f"Primary Investigator Phone: {primary_investigator_phone}")
print(f"Primary Investigator Email: {primary_investigator_email}")
print(f"Sponsor Name: {sponsor_name}")
print(f"Sponsor Address: {sponsor_address}")
print(f"Sites of Study: {sites_of_study}")

