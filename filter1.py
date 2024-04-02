import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel(r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Albin_Benny_April_02_2024.xlsx')

# Perform filtering based on specific conditions
filtered_df = df[df['Country of recruitment'].str.contains('India', na=False)]

# Save the filtered DataFrame to a new Excel file
output_filtered_file = r'C:\Users\Anasiya\Downloads\ALL_Records_CTRI\Filtered_Countries_India_Albin_Benny_April_02_2024.xlsx'
filtered_df.to_excel(output_filtered_file, index=False)
