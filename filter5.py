import pandas as pd
# Load the previously filtered Excel file into a new DataFrame
filtered_df = pd.read_excel(r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Interventional_Albin_Benny_April_02_2024.xlsx')

# Perform the next filter based on specific conditions
# Perform the next filter based on specific conditions
next_filtered_df = filtered_df[(filtered_df['Phase of Trial'] == 'Phase 2') |
                                (filtered_df['Phase of Trial'] == 'Phase 3') |
                                (filtered_df['Phase of Trial'] == 'Phase 2/ Phase 3')]

# Save the next filtered DataFrame to a new Excel file
output_next_filtered_file = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Phase2_3_Albin_Benny_April_02_2024.xlsx'
next_filtered_df.to_excel(output_next_filtered_file, index=False)
