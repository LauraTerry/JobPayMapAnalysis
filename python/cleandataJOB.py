import pandas as pd

# Read the CSV file into a DataFrame
Jobdf = pd.read_csv("data/oes_research_2023_allsectors.csv")

# Filter columns to keep
columns_to_keep = ['AREA_TITLE', 'OCC_CODE', 'A_MEDIAN']
Jobdf_filtered = Jobdf[columns_to_keep]

# Filter by job
codes_to_keep = ('11-0000', '13-0000', '15-0000', '17-0000', '19-0000', '21-0000', '23-0000', '25-0000', '27-0000', '29-0000', 
                 '31-0000', '33-0000', '35-0000', '37-0000', '39-0000', '41-0000', '43-0000', '45-0000', '47-0000', '49-0000', 
                 '51-0000', '53-0000')

# Filter rows by job codes
filtered_df = Jobdf_filtered[Jobdf_filtered['OCC_CODE'].isin(codes_to_keep)]

# Replace null values in 'A_MEDIAN' column
replacement_null = {'*': '#'}
filtered_df['A_MEDIAN'].replace(replacement_null, inplace=True)

# Remove commas from 'A_MEDIAN'
filtered_df['A_MEDIAN'] = filtered_df['A_MEDIAN'].str.replace(',', '', regex=False)

# Rename columns in filtered DataFrame
filtered_df = filtered_df.rename(columns={'AREA_TITLE': 'State', 'OCC_CODE': 'Job type', 'A_MEDIAN': 'Annual Median Income'})

# Normalize state names by stripping extra spaces and converting to uppercase
filtered_df['State'] = filtered_df['State'].str.strip().str.upper()

# Drop entries for Puerto Rico and Guam
exclude_states = ['PUERTO RICO', 'GUAM', 'VIRGIN ISLANDS', 'DISTRICT OF COLUMBIA']
filtered_df = filtered_df[~filtered_df['State'].isin(exclude_states)]

# Map general job titles to codes
job_type_mapping = {
    '11-0000': 'Management',
    '13-0000': 'Business and Financial',
    '15-0000': 'Technology and Mathematics',
    '17-0000': 'Engineering',
    '19-0000': 'Scientific Research',
    '21-0000': 'Social Services',
    '23-0000': 'Legal Occupations',
    '25-0000': 'Education',
    '27-0000': 'Arts and Media',
    '29-0000': 'Healthcare Practitioners',
    '31-0000': 'Healthcare Support',
    '33-0000': 'Protective Services',
    '35-0000': 'Food Service',
    '37-0000': 'Maintenance and Cleaning',
    '39-0000': 'Personal Care and Service',
    '41-0000': 'Sales',
    '43-0000': 'Office and Administrative',
    '45-0000': 'Farming and Forestry',
    '47-0000': 'Construction',
    '49-0000': 'Installation and Repair',
    '51-0000': 'Production Occupations',
    '53-0000': 'Transportation and Moving'
}

# Replace job codes with descriptions
filtered_df['Job type'] = filtered_df['Job type'].replace(job_type_mapping)

# Save filtered DataFrame to a new CSV file
filtered_df.to_csv('data/Jobfiltered_data.csv', index=False)

# Display the filtered DataFrame
print(filtered_df.head())
