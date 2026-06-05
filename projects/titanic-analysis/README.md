# Titanic Survival Analysis

## Progress So Far

### Dataset Exploration

The dataset was loaded and explored using Pandas to understand its structure, data types, and missing values.

The following checks were performed:

- Dataset shape
- Column names
- Data types
- Statistical summary
- Missing value analysis

---

### Missing Value Analysis

A missing value percentage table was created to identify columns requiring cleaning.

#### Findings

Column    Missing Percentage 
Cabin     78.23% 
Age       20.57% 
Fare      0.24% 

---

### Data Cleaning

The following cleaning decisions were made:

| Column | Action |
|----------|----------|
| Cabin | Removed |
| Age | Filled using Median |
| Fare | Filled using Median |
| Name | Removed |
| Ticket | Removed |
| PassengerId | Removed |
| Embarked | Retained |

#### Reasons

- Cabin contained excessive missing values and was removed.
- Age was retained because it is important for survival analysis.
- Median was used for Age and Fare because it is less affected by outliers.
- Name, Ticket, and PassengerId do not directly contribute to survival analysis in their raw form.
- Embarked may provide useful information regarding passenger boarding location.

---

### Hypotheses Before Analysis

1. Female passengers may have had a higher survival rate than male passengers.

2. Younger passengers may have had different survival rates compared to adults.

3. Passengers traveling with family members may have experienced different survival outcomes than those traveling alone.

4. First-class passengers may have had higher survival rates than third-class passengers.

---

---

## Exploratory Data Analysis (EDA)

### Hypothesis 1: Gender and Survival

**Observation:**
- Female survival rate: 74.2%
- Male survival rate: 18.9%

**Conclusion:**
The analysis supports the hypothesis. Female passengers had a significantly higher survival rate than male passengers.

---

### Hypothesis 2: Age and Survival

**Observation:**
- The average age of survivors was approximately 28 years.
- Younger passengers generally showed better survival outcomes than older passengers.
- The youngest age group had the highest survival rate.

**Conclusion:**
The analysis supports the hypothesis. Age appears to have influenced survival outcomes.

---

### Hypothesis 3: Family and Survival

**Observation:**
- Passengers travelling with family had a survival rate of approximately 50.6%.
- Passengers travelling alone had a survival rate of approximately 30.4%.
- Medium-sized families generally showed better survival outcomes than passengers travelling alone.

**Conclusion:**
The analysis supports the hypothesis. Travelling with family was associated with a higher survival rate.

---

### Hypothesis 4: Passenger Class and Survival

**Observation:**
- Class 1 survival rate: 63.0%
- Class 2 survival rate: 47.3%
- Class 3 survival rate: 24.2%
- Class 3 contained the highest number of passengers.

**Conclusion:**
The analysis supports the hypothesis. First-class passengers had a much higher survival rate than third-class passengers.

## Key Insights

1. Female passengers were significantly more likely to survive than male passengers.
2. Younger passengers generally had better survival outcomes than older passengers.
3. Passengers travelling with family members had higher survival rates than passengers travelling alone.
4. First-class passengers had the highest survival rate, while third-class passengers had the lowest.
5. Although third-class passengers made up the largest group on the ship, they experienced the poorest survival outcomes.
6. Passenger class, gender, age, and family size all appear to be important factors influencing survival.

## Machine Learning Phase

### Features Used

The following features were selected for model training:

- Pclass
- Sex
- Age
- Fare
- Embarked
- FamilySize

### Data Preprocessing

- Missing values were handled during the cleaning phase.
- Categorical variables (Sex and Embarked) were encoded into numerical values.
- Feature matrix (X) and target variable (y) were created.
- Dataset was split into training and testing sets using an 80:20 ratio.

### Models Trained

The following classification models were trained and evaluated:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
4. K-Nearest Neighbors (KNN)

### Model Performance

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 80% |
| Decision Tree | 76% |
| Random Forest | 81% |
| KNN | 73% |

### Best Model

Random Forest achieved the highest accuracy of 81% and was selected as the final model for predicting Titanic passenger survival.

### Key Findings

- Female passengers had significantly higher survival rates than male passengers.
- First-class passengers had much higher survival rates than third-class passengers.
- Passengers traveling with family generally had better survival chances than those traveling alone.
- Younger passengers showed higher survival rates than most adult groups.
- Passenger class appeared to have a stronger impact on survival than embarkation port.

### Final Conclusion

This project demonstrates a complete machine learning workflow including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Hypothesis Testing
- Feature Engineering
- Data Preprocessing
- Model Training
- Model Evaluation
- Model Comparison

The Random Forest model achieved the best performance with an accuracy of 81%.

## Conclusions

Through exploratory data analysis and hypothesis testing, several factors influencing passenger survival were identified.

Key findings include:

- Female passengers had a significantly higher survival rate than male passengers.
- First-class passengers were much more likely to survive than third-class passengers.
- Passengers traveling with family generally had better survival chances than those traveling alone.
- Younger passengers showed higher survival rates compared to many adult age groups.
- Passenger class had a stronger impact on survival than embarkation port.

These findings support the historical understanding that priority was often given to women, children, and higher-class passengers during the evacuation process.

---

## Machine Learning Model

After completing data cleaning, feature engineering, and exploratory analysis, multiple machine learning models were trained to predict passenger survival.

The following models were evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)

### Model Performance

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 80% |
| Decision Tree | 76% |
| Random Forest | 81% |
| KNN | 73% |

Among all tested models, the Random Forest Classifier achieved the highest accuracy of 81% and was selected as the final model.

This project demonstrates a complete machine learning workflow, including data preprocessing, feature engineering, model training, model evaluation, and model comparison.

## Feature Importance

A Random Forest model was used to measure feature importance.

Top predictive features:

1. Fare
2. Sex
3. Age
4. FamilySize
5. Pclass
6. Embarked

The feature importance analysis confirmed many of the insights discovered during EDA, particularly the influence of passenger gender, age, and socioeconomic status on survival.

## Current Status

- [x] Dataset Exploration
- [x] Missing Value Analysis
- [x] Data Cleaning
- [x] Hypothesis Generation
- [x] Exploratory Data Analysis (EDA)
- [x] Visualizations
- [x] Insights
- [x] Feature Engineering
- [x] Machine Learning Model
- [x] Model Evaluation
- [x] Model Comparison
- [x] Final Conclusions
- [x] Project Documentation
- [x] Conclusions
- [x] Machine Learning Model (Optional)
