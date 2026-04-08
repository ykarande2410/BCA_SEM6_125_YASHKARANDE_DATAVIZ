# Data Visualization with Tips Dataset
# This program demonstrates various data visualization techniques using matplotlib and seaborn
# including scatter plots, line charts, bar charts, and histograms

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the tips dataset from CSV file containing restaurant bill and tip information
df = pd.read_csv("C:/Users/adity/OneDrive/Desktop/Data_Visualization_Practice/unit3/tips.csv")

# Configure seaborn styling with a clean whitegrid background for better aesthetics
sns.set(style="whitegrid")

# =====================================================
# 1. Scatter Plot: Relationship between Bill and Tip
# =====================================================
# Visualize the correlation between total bill amount and tip amount
# Scatter plots are ideal for showing relationships between two continuous variables
plt.figure()
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title("Scatter Plot: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# =====================================================
# 2. Line Chart: Trend Analysis
# =====================================================
# Sort data by total bill to create a meaningful trend line
# Line charts help visualize trends over ordered data
df_sorted = df.sort_values(by='total_bill')

plt.figure()
plt.plot(df_sorted['total_bill'], df_sorted['tip'], marker='o')
plt.title("Line Chart: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# =====================================================
# 3. Bar Chart: Categorical Comparison
# =====================================================
# Compare average tip amounts across different gender categories
# Bar charts are effective for comparing values across categories
plt.figure()
sns.barplot(x='sex', y='tip', data=df)
plt.title("Bar Chart: Average Tip by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Tip")
plt.show()

# =====================================================
# 4. Histogram: Distribution Analysis
# =====================================================
# Show the frequency distribution of total bill amounts
# Includes KDE (kernel density estimation) curve for smooth distribution visualization
plt.figure()
sns.histplot(df['total_bill'], bins=5, kde=True)
plt.title("Histogram: Total Bill Distribution")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()