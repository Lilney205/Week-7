# Import necessary libraries
import pandas as pd
import numpy as np

# Task 1: Load the dataset
# Load your dataset in CSV format (for example, 'sales_data.csv')
try:
    data = pd.read_csv('sales_data.csv')  # Replace with the actual dataset path
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    
# Display the first few rows to inspect the data
print(data.head())

# Check the data types and missing values
print(data.info())
print(data.isnull().sum())

# Clean the dataset by either filling or dropping missing values
# Option 1: Drop missing values
data_cleaned = data.dropna()

# Option 2: Fill missing values (example using the mean)
data_cleaned = data.fillna(data.mean())
