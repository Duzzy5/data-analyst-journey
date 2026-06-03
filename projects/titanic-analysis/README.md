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


## Current Status

- [x] Dataset Exploration
- [x] Missing Value Analysis
- [x] Data Cleaning
- [x] Hypothesis Generation
- [x] Exploratory Data Analysis (EDA)
- [x] Visualizations
- [x] Insights
- [ ] Feature Engineering
- [ ] Machine Learning Model
- [ ] Model Evaluation
- [ ] Model Comparison
- [ ] Final Conclusions
- [ ] Project Documentation
- [ ] Conclusions
- [ ] Machine Learning Model (Optional)
