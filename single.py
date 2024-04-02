import pandas as pd
import re

# Read the CSV file into a DataFrame
file_path = r"C:\Users\Anasiya\Downloads\ALL_Records_CTRI\CTRI_Database_part2_39,970 items\MjA0MDA.csv"
df = pd.read_csv(file_path, delimiter=',', header=None, names=['data'])

# Join lines that belong together
df['data'] = df['data'].replace('\n', ' ', regex=True)

# Extract CTRI Number, Registered on Date, Type of Trial, Type of Study, and Phase of Trial
df['CTRI Number'] = df['data'].str.extract(r'CTRI Number\s*:\s*([^\[]+)')
df['Registered on Date'] = df['data'].str.extract(r'Registered on\s*:\s*([\d/]+)')
df['Type of Trial'] = df['data'].str.extract(r'Type of Trial\s*:\s*([^\n]+)')
df['Type of Study'] = df['data'].str.extract(r'Type of Study\s*:\s*([^\n]+)')
df['Phase of Trial'] = df['data'].str.extract(r'Phase\s*:\s*([^\n]+)')

# Print the extracted information
print(df[['CTRI Number', 'Registered on Date', 'Type of Trial', 'Type of Study', 'Phase of Trial']])
