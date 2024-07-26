import pandas as pd
import numpy as np
import psycopg2 as pg


# Read the CSV file into a DataFrame
COLdata = pd.read_csv('data/cost_of_living_us.csv')

# Filter the DataFrame to select only rows where family_member_count is '1p0c'
filtered_data = COLdata[COLdata['family_member_count'] == '1p0c']

# Select the relevant columns
results = filtered_data[["state", "family_member_count", "housing_cost", "total_cost", "median_family_income"]]

# Reset the index of the DataFrame
results.reset_index(drop=True, inplace=True)

# Save the filtered DataFrame to a new CSV file
results.to_csv("data/COLdataset1p0c.csv", index=False)

# COLdata= pd.read_csv('data/cost_of_living_us.csv')

# state =  COLdata.groupby(['family_member_count', 'median_family_income'])
# types= COLdata.state.dtype

# results = COLdata[["state", "family_member_count", "housing_cost", "total_cost", "median_family_income"]]

# results.reset_index(drop = True, inplace = True)
# results.to_csv("data/COLdataset.csv")

#Descriptions of columns
## family = ['1p0c' '1p1c' '1p2c' '1p3c' '1p4c' '2p0c' '2p1c' '2p2c' '2p3c' '2p4c']
# ##['case_id', 'state', 'isMetro', 'areaname', 'county',
#        'family_member_count', 'housing_cost', 'food_cost',
#        'transportation_cost', 'healthcare_cost', 'other_necessities_cost',
#        'childcare_cost', 'taxes', 'total_cost', 'median_family_income'],  
# case_id                     int64
# state                      object
# isMetro                      bool
# areaname                   object
# county                     object
# family_member_count        object
# housing_cost              float64
# food_cost                 float64
# transportation_cost       float64
# healthcare_cost           float64
# other_necessities_cost    float64
# childcare_cost            float64
# taxes                     float64
# total_cost                float64
# median_family_income      float64