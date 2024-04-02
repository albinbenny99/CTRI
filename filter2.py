import pandas as pd
# Load the previously filtered Excel file into a new DataFrame
filtered_df = pd.read_excel(r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Filtered_Countries_India_Albin_Benny_April_02_2024.xlsx')

# Convert 'Registered on Date' column to datetime
filtered_df['Registered on Date'] = pd.to_datetime(filtered_df['Registered on Date'], format='%d/%m/%Y')

# Perform the next filter based on specific conditions
next_filtered_df = filtered_df[filtered_df['Registered on Date'] >= '2019-04-01']

# Save the next filtered DataFrame to a new Excel file
output_next_filtered_file = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Registered_After_April_1_2019_Albin_Benny_April_02_2024.xlsx'
next_filtered_df.to_excel(output_next_filtered_file, index=False)
