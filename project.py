import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dummy sales data generate karna
np.random.seed(42)
data = {
    'Product': np.random.choice(['A', 'B', 'C', 'D'], 50),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 50),
    'Sales': np.random.randint(100, 1000, 50)
}
df = pd.DataFrame(data)

# Basic data dekhna
print(df.head())

                              
product_sales = df.groupby('Product')['Sales'].sum()
print("### Data Sample")
print(df.head())

# Product-wise sales summation
product_sales = df.groupby('Product')['Sales'].sum()
print("\n### Product-wise Total Sales")
print(product_sales)

# Region-wise sales summation
region_sales = df.groupby('Region')['Sales'].sum()
print("\n### Region-wise Total Sales")
print(region_sales)

# Bar plot for product sales
plt.figure(figsize=(8, 6))
product_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Pie plot for region sales
plt.figure(figsize=(8, 6))
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales Distribution by Region')
plt.ylabel('')
plt.show()