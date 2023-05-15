import pandas as pd

# Read the CSV file into a pandas dataframe
data = pd.read_csv("./data/sample_data.csv", delimiter=";")

# Calculate the mean, 25th, 50th, and 75th percentile for each column
mean = data.mean()
percentile_25 = data.quantile(0.25)
percentile_50 = data.quantile(0.5)
percentile_75 = data.quantile(0.75)

# Print the results
print("Mean values:")
print(mean)
print("\n25th percentile values:")
print(percentile_25)
print("\n50th percentile values:")
print(percentile_50)
print("\n75th percentile values:")
print(percentile_75)


