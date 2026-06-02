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

## Current Status

- [x] Dataset Exploration
- [x] Missing Value Analysis
- [x] Data Cleaning
- [x] Hypothesis Generation
- [ ] Exploratory Data Analysis (EDA)
- [ ] Visualizations
- [ ] Insights
- [ ] Conclusions
- [ ] Machine Learning Model (Optional)
