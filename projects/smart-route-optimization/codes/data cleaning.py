# Dataset cleaning

print(df.info)
df.isnull().sum()

# dataset dose not contain any null values 

#  Checking outliers 

Q1 = df["Distance (km)"].quantile(0.25)
Q3 = df["Distance (km)"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("Lower Limit :", lower)
print("Upper Limit :", upper)

outliers = df[
    (df["Distance (km)"] < lower) |
    (df["Distance (km)"] > upper)
]

print(outliers)
# our dataset had outiers but the outliers in such cases where possible so due to such reason their was no need for data cleaning in our dataset
