# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: transactions.csv with columns: Date, Category, Amount
# Example:
# Date,Category,Amount
# 2025-01-05,Food,250
# 2025-01-06,Travel,500

# Load data
df = pd.read_csv('transactions.csv', parse_dates=['Date'])

# Add Month column
df['Month'] = df['Date'].dt.to_period('M')

# Monthly spending trend
monthly_trend = df.groupby('Month')['Amount'].sum()
print("Monthly Spending Trend:\n", monthly_trend)

# Category-wise spending trend
category_trend = df.groupby('Category')['Amount'].sum()
print("\nCategory-wise Spending Trend:\n", category_trend)

# Plot monthly trend
plt.figure(figsize=(10,5))
monthly_trend.plot(kind='bar', color='skyblue')
plt.title('Monthly Spending Trend')
plt.ylabel('Total Amount Spent')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.show()

# Plot category-wise trend
plt.figure(figsize=(8,5))
category_trend.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Category-wise Spending Distribution')
plt.ylabel('')
plt.show()
