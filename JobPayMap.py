import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# # Load the job data
job_data = pd.read_csv('data/Merged_dataset.csv')

# # Load the shapefile of US states
shapefile = gpd.read_file('data/States_shapefile.shp')
print(shapefile.columns)

# Ensure state names are uppercase in both datasets
job_data['state'] = job_data['state'].str.upper()
shapefile['State_Name'] = shapefile['State_Name'].str.upper()

# Display available vocations to the user
print("Available vocations:")
vocations = job_data['Job Type'].unique()

#reindex the vocations in a new numbered list
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
merged_data = shapefile.merge(filtered_data, left_on='State_Name', right_on='state')

# Reproject to Albers contiguous USA
merged_data = merged_data.to_crs("ESRI:102003")

# # Plot the heatmap
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='Percentage_Income_Leftover', ax=ax, legend=True,
                 legend_kwds={'label': "Residual Income by State (%)",
                              'orientation': "horizontal"},
                 # Color map: red-yellow-green
                 cmap='RdYlGn', 
                 edgecolor='black')

# Set plot title and remove axis
plt.title(f'Residual Income by State for {selected_vocation}')
ax.set_axis_off()

# Show plot
plt.show()