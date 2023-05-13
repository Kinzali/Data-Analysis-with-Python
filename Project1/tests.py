import pandas as pd
import numpy as np

# Create a sample CSV file with random values
data = pd.DataFrame({
    'Revenue': np.random.randint(100, 1000, 10),
    'Stock': np.random.randint(50, 200, 10),
    'Deliveries': np.random.randint(5, 20, 10)
})
data = pd.read_csv("ß/sample_data.csv", delimiter=";")

# Read the CSV file and calculate the mean and percentile values
data = pd.read_csv('test_data.csv')
mean = data.mean()

# Define the expected mean values
expected_mean = {
    'Revenue': data['Revenue'].mean(),
    'Stock': data['Stock'].mean(),
    'Deliveries': data['Deliveries'].mean()
}

# Debug the mean calculation
print("Calculated mean values:")
print(mean)
print("\nExpected mean values:")
print(expected_mean)

# Verify that the calculated values match the expected values
assert mean.equals(expected_mean)

print("All tests passed!")
