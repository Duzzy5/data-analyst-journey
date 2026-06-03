#Hypothesis 1:-Female passengers may have had a higher survival rate than male passengers.
print(df_cleaned["Sex"].value_counts()) # Tells total number of male and female
(df_cleaned.groupby("Sex")["Survived"].mean() * 100)
print(f"Female Survival Rate: {survival_rate['female']:.2f}%")
print(f"Male Survival Rate: {survival_rate['male']:.2f}%")
pd.crosstab(df_cleaned["Sex"], df_cleaned["Survived"])

import matplotlib.pyplot as plt

(df_cleaned.groupby("Sex")["Survived"].mean() * 100).plot(kind="bar")
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate (%)")
plt.show()



#hypothesis 2:- Younger passengers may have had different survival rates compared to adults.
df_cleaned["Age"].hist(bins=20)
df_cleaned.groupby("Survived")["Age"].mean()

df_cleaned["AgeGroup"] = pd.cut(
    df_cleaned["Age"],
    bins=[0,18,30,50,100],
    labels=["0-18","18-30","30-50","50+"]
)
print(df_cleaned.groupby("AgeGroup")["Survived"].mean()*100)

df_cleaned[df_cleaned["Survived"]==1]["Age"].value_counts()
df_cleaned.groupby("AgeGroup")["Survived"].mean()
(df_cleaned.groupby("AgeGroup")["Survived"].mean() * 100).plot(kind="bar")




Hypothesis 3:-Passengers traveling with family members may have experienced different survival outcomes than those traveling alone.
df_cleaned["FamilySize"] = (
    df_cleaned["SibSp"] +
    df_cleaned["Parch"]
)
print(f"People traveling alone are {(df_cleaned["FamilySize"] == 0).sum()}")
print(f"rate of people who survived alone {df_cleaned[df_cleaned["FamilySize"] == 0]["Survived"].mean() * 100}")
print(f"People traveling with family are {(df_cleaned["FamilySize"] > 0).sum()}")
print(f"survival rate of who were traveling with family are {df_cleaned[df_cleaned["FamilySize"] > 0]["Survived"].mean() * 100}")

family_survival = (
    df_cleaned
    .assign(FamilyType=lambda x:
            x["FamilySize"].apply(
                lambda y: "Alone" if y == 0 else "With Family"
            ))
    .groupby("FamilyType")["Survived"]
    .mean() * 100
)
family_survival.plot(kind="bar")
(df_cleaned.groupby("FamilySize")["Survived"].mean() * 100).plot(
    kind="bar",
    figsize=(8,4)
)



#Hypothesis 4:- First-class passengers may have had higher survival rates than third-class passengers.
df_cleaned["Pclass"].value_counts().sort_index()
df_cleaned["Pclass"].value_counts().sort_index().plot(kind="bar")

print(df_cleaned.groupby("Pclass")["Survived"].mean() * 100)
pd.crosstab(
    df_cleaned["Pclass"],
    df_cleaned["Survived"]
)

import matplotlib.pyplot as plt

survival_rate = (
    df_cleaned.groupby("Pclass")["Survived"].mean() * 100
)

ax = survival_rate.plot(
    kind="bar",
    figsize=(6,4)
)

plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.ylim(0, 100)

# Add percentage labels
for i, value in enumerate(survival_rate):
    plt.text(i, value + 2, f"{value:.1f}%", ha="center")

plt.show()
