import pandas as pd
# Load the previously filtered Excel file into a new DataFrame
filtered_df = pd.read_excel(r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Registered_Prospectively_Albin_Benny_April_02_2024.xlsx')

# Perform the next filter based on specific conditions
next_filtered_df = filtered_df[filtered_df['Trial Type'] == 'Interventional']

# Save the next filtered DataFrame to a new Excel file
output_next_filtered_file = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Interventional_Albin_Benny_April_02_2024.xlsx'
next_filtered_df.to_excel(output_next_filtered_file, index=False)
