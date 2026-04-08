# Smartphone Usage and Productivity Dataset Analysis
# This program explores and analyzes a smartphone usage productivity dataset
import pandas as pd

# Load the smartphone usage and productivity dataset from CSV file
df=pd.read_csv("C:/Users/ASUS/Downloads/IPL.csv")

# Display the first 10 records from the dataset
print("first 10 rescords",df.head(10))
print("-----------------------------------------        -----------------------------")
# Display the last 10 records from the dataset
print("last 10 records",df.tail(10))

print("----------------------")
# Print all column names in the dataset
print("columns in dataset::",df.columns)
print("--------------------------------------")
# Display the shape of the dataset (number of rows and columns)
print("number of rows and columns::",df.shape)
print("--------------------------------------")
# Show the data type of each column (int, float, string, etc.)
print("data types of columns::",df.dtypes)
print("--------------------------------------")
# Count the number of missing/null values in each column
print("number of missing values in each column::",df.isnull().sum())
print("--------------------------------------")
# Display 20 random records for sample analysis
print("random 20 records:",df.sample(20))
print("--------------------------------------  ")
# Print comprehensive statistical summary (mean, std, min, max, quartiles)
print("statistical summary of dataset::",df.describe())
print("--------------------------------------")
print("------------------------")

# Add a new column "RUNS" with the default value "HIGH" to all records
new_col=df["RUNS"]="HIGH"
print(new_col)
# Display the newly created Runs column
print(df["RUNS"])