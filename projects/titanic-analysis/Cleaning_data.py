#Titanic Dataset

#Loading Dataset
import pandas as pd
df = pd.read_csv("C:\\datasets\\tested.csv")
df.head()         #shows 1st 5 rows
df.tail()         #shows last 5 rows
df.shape          #tells no. of rows then columns 
df.columns        #gives name of every column
df.info()         # gives non null count of every column along with datatype
df.describe()     # gives statistical information about every column
df.isnull().sum()

#Finding Percentages of missing values in a column
missing_value=df.isnull().sum()
missing_percentage = (missing_value/len(df))*100
missing_data=pd.DataFrame({
    "Missing Value":missing_values,
    "Percentage":missing_percentage
})
missing_data.sort_values(by="Percentage",ascending=False)

#Dataset cleaning:- removing columns and handling missing values 
df_cleaned=df.copy()
df_cleaned = df_cleaned.drop("Cabin",axis=1)
df_cleaned["Fare"]=df_cleaned["Fare"].fillna(df["Fare"].median())
df_cleaned["Age"]=df_cleaned["Age"].fillna(df["Age"].median())
df_cleaned= df_cleaned.drop("Name",axis=1## Hypotheses Before Analysis
df_cleaned= df_cleaned.drop("Ticket",axis=1)
df_cleaned= df_cleaned.drop(["PassengerId"],axis=1)
print(f"Original Dataset Shape: {df.shape}")
print(f"Cleaned Dataset Shape: {df_cleaned.shape}")
