# Statistical Analysis and Data Exploration
# This program demonstrates basic statistical operations on datasets using pandas
import pandas as pd


# Create a sample dataset with student information
students={
    "name":["a","b","c"],   
    "graduation_percentage":[80,85,90],
    "age":[20,21,22],

}
# Convert dictionary to DataFrame for tabular data representation
df=pd.DataFrame(students)
print("--------------------------------------")
print(df)  # Display the student dataframe
print("--------------------------------------")
# Calculate average age of students
print( "to calculate mean(average) of age column::",df["age"].mean())
print("--------------------------------------")
# Calculate average graduation percentage
print("#to calculate mean(average) of graduation percentage column:",df["graduation_percentage"].mean()) 
print("--------------------------------------")
# Display comprehensive statistical summary (count, mean, std, min, max, quartiles)
print("#describe all basic statistics of data::",df.describe())

print("--------------------------------------")
# Load iris dataset from CSV file
df=pd.read_csv("C:\\Users\\ASUS\\\Downloads\\IRIS.csv")
# Display the loaded dataframe
print(pd.DataFrame(df))
print("--------------------------------------")

# Display statistical summary of all columns in iris dataset
print(df.describe())
print("--------------------------------------")

# Calculate the mean (average) age from the iris dataset
print("Mean age::",df[ "Age"].mean())
print("--------------------------------------")
# Calculate the median stress level
print("Median Stress_Level::",df["Stress_Level"].median())
print("--------------------------------------")
# Calculate the range of age (max - min)
print("range of aage::",df["Age"].max()-df["Age"].min())
print("--------------------------------------")
# Calculate the standard deviation of stress level (measures data spread)
print("standard deviation::",df["Stress_Level"].std())

print("--------------------------------------")
# Calculate the variance of stress level (squared standard deviation)
print("variance of stress level::",df["Stress_Level"].var())

print("--------------------------------------")
# Sample 1000 random records from the dataset for analysis
print("random records",df.sample(1000))
print("--------------------------------------   ")    
# Display all unique gender values in the dataset
print(df["Gender"].unique())
print("--------------------------------------   ")
