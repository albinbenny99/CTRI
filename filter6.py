import pandas as pd
# Load the previously filtered Excel file into a new DataFrame
filtered_df = pd.read_excel(r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Phase2_3_Albin_Benny_April_02_2024.xlsx')

# Perform the next filter based on specific conditions
next_filtered_df = filtered_df[(filtered_df['Recruitment Status in India'] == 'Closed to Recruitment of Participants') |
                                (filtered_df['Recruitment Status in India'] == 'Completed')]

# Save the next filtered DataFrame to a new Excel file
output_next_filtered_file = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Recruitment_Closed_Completed_Albin_Benny_April_02_2024.xlsx'
next_filtered_df.to_excel(output_next_filtered_file, index=False)
