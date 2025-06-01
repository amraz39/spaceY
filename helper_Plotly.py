import pandas as pd

# Load the dataset
df = pd.read_csv('spacex_launch_dash.csv')

# Filter for successful launches
successful_launches = df[df['class'] == 1]

# Count successful launches per site
site_success_counts = successful_launches['Launch Site'].value_counts()

# Identify the site with the most successful launches
most_successful_site = site_success_counts.idxmax()
print(f"Site with the most successful launches: {most_successful_site}")

# Calculate success rate per site
site_success_rate = df.groupby('Launch Site')['class'].mean()

# Identify the site with the highest success rate
highest_success_rate_site = site_success_rate.idxmax()
print(f"Site with the highest launch success rate: {highest_success_rate_site}")

# Define payload bins
bins = [0, 2000, 4000, 6000, 8000, 10000]
labels = ['0-2k', '2k-4k', '4k-6k', '6k-8k', '8k-10k']

# Create a new column for payload range
df['Payload Range'] = pd.cut(df['Payload Mass (kg)'], bins=bins, labels=labels, right=False)

# Calculate success rate per payload range
payload_success_rate = df.groupby('Payload Range')['class'].mean()

# Identify the payload range with the highest success rate
highest_success_rate_payload = payload_success_rate.idxmax()
print(f"Payload range with the highest success rate: {highest_success_rate_payload}")

# Identify the payload range with the lowest success rate
lowest_success_rate_payload = payload_success_rate.idxmin()
print(f"Payload range with the lowest success rate: {lowest_success_rate_payload}")

# Calculate success rate per booster version
booster_success_rate = df.groupby('Booster Version Category')['class'].mean()

# Identify the booster version with the highest success rate
highest_success_rate_booster = booster_success_rate.idxmax()
print(f"Booster version with the highest success rate: {highest_success_rate_booster}")