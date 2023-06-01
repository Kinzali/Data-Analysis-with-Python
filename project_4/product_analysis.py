# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define a sample product data
data = {'year': [2019, 2019, 2019, 2020, 2020, 2020, 2021, 2021, 2021],
        'product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
        'revenue': [1000, 2000, 3000, 1500, 2500, 3500, 1200, 2200, 3200],
        'profit': [100, 200, 300, 150, 250, 350, 120, 220, 320]}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# View the DataFrame
print(df)

# Calculate the total revenue and profit for each year
yearly_revenue = df.groupby('year')['revenue'].sum()
yearly_profit = df.groupby('year')['profit'].sum()

# View the yearly revenue and profit
print(yearly_revenue)
print(yearly_profit)

# Calculate the revenue and profit margin for each year
yearly_margin = df.groupby('year').apply(lambda x: np.mean(x['profit']/x['revenue']))
yearly_margin = yearly_margin.rename('margin').reset_index()

# View the yearly margin
print(yearly_margin)

# Visualize the revenue and profit trends for each year
sns.lineplot(data=yearly_revenue)
plt.title('Yearly Revenue Trend')
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.show()

sns.lineplot(data=yearly_profit)
plt.title('Yearly Profit Trend')
plt.xlabel('Year')
plt.ylabel('Profit')
plt.show()

sns.lineplot(data=yearly_margin, x='year', y='margin')
plt.title('Yearly Profit Margin Trend')
plt.xlabel('Year')
plt.ylabel('Profit Margin')
plt.show()
