# S-1 feature selection
features = [
    "Pclass",
    "Sex",
    "Age",
    "Fare",
    "Embarked",
    "FamilySize"
]

target = ["Survived"]

#S-2 Convert Text to Numbers
from sklearn.preprocessing import LabelEncoder

le_sex = LabelEncoder()
le_embarked = LabelEncoder()

df_cleaned["Sex"] = le_sex.fit_transform(df_cleaned["Sex"])
df_cleaned["Embarked"] = le_embarked.fit_transform(df_cleaned["Embarked"])

#S-3 Create X and y
X = df_cleaned[features]
y = df_cleaned["Survived"]

#S-4 Train Test and Split
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#S-5 Train Model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)

#S-6 Make Predictions
predictions = model.predict(X_test)

#S-7 Evaluate Model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,predictions)
print(accuracy)

#S-8 Trying different models

#Decisiom Tree Classifier
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Decision Tree Accuracy:", accuracy)

#Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Random Forest Accuracy:", accuracy)

# KNN
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("KNN Accuracy:", accuracy)
