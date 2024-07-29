import pandas as pd

# #merge the cleaned datasets using state as key
Cost_of_living_df = pd.read_csv("data/COL1p0c.csv")
Job_Income_df = pd.read_csv("data/Jobsfiltered.csv")

# Convert state names to uppercase in both DataFrames
Cost_of_living_df['state'] = Cost_of_living_df['state'].str.upper()
Job_Income_df['state'] = Job_Income_df['state'].str.upper()

# Merge the datasets
merged_df = pd.merge(Cost_of_living_df, Job_Income_df, on='state', how='inner')

# # Calculate the net income
merged_df['Net_Income'] = merged_df['avg_income'] - merged_df['Cost of Living']

#Calculate the percentage of residual income 
merged_df['Percentage_Income_Leftover'] = (merged_df['Net_Income'] / merged_df['avg_income'] * 100).round()

# # Save the merged dataframe to a new CSV file
merged_df.to_csv('data/Merged_dataset.csv', index=False)
