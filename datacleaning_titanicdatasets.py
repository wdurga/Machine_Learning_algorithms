# -*- coding: utf-8 -*-
"""DataCleaning_titanicDataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V0-j6KGxraRcO0X_ZrsLjQ2C864309Jv

To perform data cleaning on the Titanic dataset by identifying and handling missing values, correcting data types, removing duplicates, and preparing the dataset for further analysis or modeling.


Dataset Description
The Titanic dataset provides information about passengers aboard the Titanic. It includes features such as:

PassengerId: Unique identifier for each passenger.
Survived: Survival status (0 = No, 1 = Yes).
Pclass: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd).
Name, Sex, Age: Demographic details.
SibSp, Parch: Number of relatives aboard.
Ticket, Fare, Cabin: Ticket details.
Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

IMPORTING LIBRARIES
"""

import pandas as pd
import numpy as np

"""LOADING DATASET"""

df = pd.read_csv("Titanic-Dataset.csv")
df.head()

"""DATASET INFORMATION"""

df.info()

"""CHECKING FOR MISSING VALUES

"""

# check missing values Column-wise

missing_values = df.isna().sum()
print("Missing values in each column : ")
print(missing_values)

# Check missing values in Rows

missing_values_row = df.isna().sum(axis=1)
print("Missing values in each row:")
print(missing_values_row)

"""HANDLING MISSING VALUES IN COLUMNS"""

# Fill missing values in 'Age' with the mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Drop 'Cabin' column due to too many missing values
df = df.drop(columns=['Cabin'])

# Fill missing values in 'Embarked' with the mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Check missing values after handling
print("Missing values after handling columns:")
print(df.isna().sum())

"""HANDLING MISSING VALUES IN ROWS"""

# Drop rows with more than a threshold of missing values (e.g., 2)
df = df[df.isna().sum(axis=1) <= 2]

# Fill remaining missing values row-wise
df['Age'] = df['Age'].fillna(df['Age'].median())    # Fill 'Age' with median
df['Embarked'] = df['Embarked'].fillna('Unknown')  # Fill 'Embarked' with a placeholder

# Check missing values after handling rows
print("Missing values after handling rows:")
print(df.isna().sum())

"""CHECK FOR DUPLICATES ROWS IN dataset"""

duplicates = df.duplicated().sum()
print("\nNumber of duplicated rows:", duplicates)

# shape of dataset
df.shape

"""CORRECTING DATA TYPES"""

df['Pclass'] = df['Pclass'].astype('category')
df['Sex'] = df['Sex'].astype('category')
df['Embarked'] = df['Embarked'].astype('category')
df['Survived'] = df['Survived'].astype(bool)

print(df.columns)

"""TO VERIFY DATA TYPES after correction"""

print("\nData types after correction : ")
print(df.dtypes)

"""CREATE ISALONE and FAMILYSIZE FEATURE"""

# Create the FamilySize feature
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1  # Add 1 to include the passenger themselves

# Create the IsAlone feature
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)  # 1 if FamilySize is 1, otherwise 0

# Display the first few rows of new feature
print(df[['SibSp', 'Parch', 'FamilySize', 'IsAlone']].head())

"""EXPORTING CLEANED DATA"""

# save cleaned data to new CSV file and excel file

# Specify the filename and path
output_file = "Titanic_cleaned_data.csv"

# Export the cleaned dataset to a CSV file
df.to_csv(output_file, index=False)

print(f"Cleaned data has been successfully exported to {output_file}")

output_file = "Titanic_cleaned_data.xlsx"

# Export the cleaned dataset to an Excel file
df.to_excel(output_file, index=False)

print(f"Cleaned data has been successfully exported to {output_file}")

