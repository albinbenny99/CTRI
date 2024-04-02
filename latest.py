import pandas as pd
import os
import glob

# Define the folder path containing all CSV files
folder_path = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Left_over_CTRI_database_34 items'


# Get a list of all CSV files in the folder
all_files = glob.glob(os.path.join(folder_path, '*.csv'))

# Define the columns you want to extract
columns = ['CTRI Number', 'Type of Trial', 'Countries of Recruitment', 
           'Recruitment Status of Trial (India)', 'Phase of Trial', 'Type of Study']

# Initialize an empty DataFrame to store the extracted data
extracted_data = pd.DataFrame(columns=columns)

# Iterate over each CSV file
for file_path in all_files:
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Check if all required columns are present in the DataFrame
    missing_columns = set(columns) - set(df.columns)
    if missing_columns:
        print(f"Columns missing in file {file_path}: {missing_columns}")
        continue
    
    # Extract the relevant information
    ctri_number = df['CTRI Number'].iloc[0]
    trial_type = df['Type of Trial'].iloc[0]
    countries = df['Countries of Recruitment'].iloc[0]
    recruitment_status = df['Recruitment Status of Trial (India)'].iloc[0]
    phase = df['Phase of Trial'].iloc[0]
    study_type = df['Type of Study'].iloc[0]
    
    # Append the extracted information to the DataFrame
    extracted_data = extracted_data.append({
        'CTRI Number': ctri_number,
        'Type of Trial': trial_type,
        'Countries of Recruitment': countries,
        'Recruitment Status of Trial (India)': recruitment_status,
        'Phase of Trial': phase,
        'Type of Study': study_type
    }, ignore_index=True)

# Save the extracted data to an Excel file
output_file_path = os.path.join(folder_path, 'extracted_data.xlsx')
extracted_data.to_excel(output_file_path, index=False)

print(f"Data extracted and saved to: {output_file_path}")
