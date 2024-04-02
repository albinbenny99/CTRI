import os
import pandas as pd







import os
import pandas as pd

# Path to the folder containing the CSV files
directory = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Left_over_CTRI_database_34 items'

# Initialize an empty list to store the extracted information
data = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)

        # Extract the desired information from each file
        ctri_number = df['CTRI Number'].iloc[0]
        registered_on = df['Registered on:'].iloc[0]
        last_modified_on = df['Last Modified On:'].iloc[0]
        trial_type = df['Type of Trial'].iloc[0]
        study_type = df['Type of Study'].iloc[0]
        public_title = df['Public Title of Study'].iloc[0]
        scientific_title = df['Scientific Title of Study'].iloc[0]
        countries_recruitment = df['Countries of Recruitment'].iloc[0]
        recruitment_status_india = df['Recruitment Status of Trial (India)'].iloc[0]
        trial_registered = df['Trial Registered'].iloc[0]

        # Append the extracted information as a dictionary
        data.append({
            'CTRI Number': ctri_number,
            'Registered on': registered_on,
            'Last Modified On': last_modified_on,
            'Type of Trial': trial_type,
            'Type of Study': study_type,
            'Public Title of Study': public_title,
            'Scientific Title of Study': scientific_title,
            'Countries of Recruitment': countries_recruitment,
            'Recruitment Status of Trial (India)': recruitment_status_india,
            'Trial Registered': trial_registered
        })

# Create a new DataFrame from the extracted information
extracted_data_df = pd.DataFrame(data)

# Save the extracted data to an Excel file
extracted_data_df.to_excel(r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\extracted_data.xlsx', index=False)

