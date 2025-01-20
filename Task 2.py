# Task 2: Compute basic statistics for numerical columns
print(data_cleaned.describe())

# Perform groupings based on a categorical column (e.g., 'region') and compute the mean for a numerical column (e.g., 'sales')
grouped_data = data_cleaned.groupby('region')['sales'].mean()
print(grouped_data)

# Identify any patterns or interesting findings
# For example, if the sales data varies significantly by region, that could be an interesting finding
