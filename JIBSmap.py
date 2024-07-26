import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the job data
job_data = pd.read_csv('data/Merged_dataset.csv')

# Load the shapefile of US states
shapefile = gpd.read_file('data/ne_10m_admin_1_states_provinces.shp')

# Ensure state names are uppercase in both datasets
job_data['state'] = job_data['state'].str.upper()
shapefile['name'] = shapefile['name'].str.upper()

#Make sure the shape file is only using the 50 US states by building a dictionary for reference
# List of 50 U.S. states
us_states = [
    'ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT',
    'DELAWARE', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA',
    'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS',
    'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
    'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA',
    'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA',
    'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
    'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'
]

# Filter shapefile to include only the 50 U.S. states
shapefile = shapefile[shapefile['name'].isin(us_states)]

# Display available vocations to the user
print("Available vocations:")
vocations = job_data['Job Type'].unique()
for i, vocation in enumerate(vocations, 1):
    print(f"{i}. {vocation}")

# Prompt the user to select a vocation
try:
    choice = int(input("Select a Job Type by number: "))
    selected_vocation = vocations[choice - 1]
except (IndexError, ValueError):
    print("Invalid choice. Exiting.")
    exit()

# Filter the dataset based on the selected vocation
filtered_data = job_data[job_data['Job Type'] == selected_vocation]

# Merge the shapefile with the filtered job data
merged_data = shapefile.merge(filtered_data, left_on='name', right_on='state')

# Plot the heatmap
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='Net_Income', ax=ax, legend=True,
                 legend_kwds={'label': "Residual Income by State",
                              'orientation': "horizontal"},
                 cmap='RdYlGn',  # Color map: red-yellow-green
                 edgecolor='black')

# Set plot title and remove axis
plt.title(f'Residual Income by State for {selected_vocation}')
ax.set_axis_off()

# Show plot
plt.show()
