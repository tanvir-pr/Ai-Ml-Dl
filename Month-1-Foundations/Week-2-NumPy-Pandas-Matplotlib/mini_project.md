# Mini Project: Titanic Dataset Exploratory Data Analysis

## Project Overview
Perform comprehensive EDA on the famous Titanic dataset to uncover insights about passenger survival patterns.

**Time:** 4-6 hours  
**Skills:** NumPy, Pandas, Matplotlib, Seaborn, Statistical Analysis

## Objectives
1. Load and explore the Titanic dataset
2. Clean and preprocess data
3. Perform statistical analysis
4. Create meaningful visualizations
5. Draw insights and conclusions

## Dataset
**Source:** https://www.kaggle.com/c/titanic/data

**Features:**
- PassengerId: Unique ID
- Survived: 0 = No, 1 = Yes
- Pclass: Ticket class (1, 2, 3)
- Name: Passenger name
- Sex: Male/Female
- Age: Age in years
- SibSp: # siblings/spouses aboard
- Parch: # parents/children aboard
- Ticket: Ticket number
- Fare: Passenger fare
- Cabin: Cabin number
- Embarked: Port (C, Q, S)

## Part 1: Data Loading & Initial Exploration

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
train = pd.read_csv('titanic_train.csv')
test = pd.read_csv('titanic_test.csv')

# TODO: Display first 10 rows
# TODO: Check shape and data types
# TODO: Display summary statistics
# TODO: Check for missing values
```

**Questions to Answer:**
1. How many passengers in the dataset?
2. What percentage survived?
3. Which features have missing values?
4. What are the data types?

## Part 2: Data Cleaning

```python
# TODO: Handle missing values
# - Age: Fill with median by Pclass
# - Embarked: Fill with mode
# - Cabin: Create 'HasCabin' feature
# - Fare: Fill with median

# TODO: Create new features
# - FamilySize = SibSp + Parch + 1
# - IsAlone = 1 if FamilySize == 1
# - Title from Name (Mr, Mrs, Miss, etc.)
# - AgeGroup (Child, Teen, Adult, Senior)

# TODO: Encode categorical variables
# - Sex: Male=1, Female=0
# - Embarked: One-hot encoding
```

## Part 3: Univariate Analysis

Analyze each feature individually:

```python
# TODO: Survival rate
# - Overall survival rate
# - Bar chart of survival counts

# TODO: Age distribution
# - Histogram with KDE
# - Box plot
# - Summary statistics

# TODO: Fare distribution
# - Histogram (log scale)
# - Outlier detection

# TODO: Categorical features
# - Bar charts for Pclass, Sex, Embarked
# - Value counts and percentages
```

## Part 4: Bivariate Analysis

Explore relationships between features:

```python
# TODO: Survival by Sex
# - Grouped bar chart
# - Survival rate by gender

# TODO: Survival by Pclass
# - Grouped bar chart
# - Chi-square test

# TODO: Survival by Age
# - Age distribution by survival
# - Violin plot

# TODO: Survival by Fare
# - Scatter plot
# - Box plot by survival

# TODO: Correlation analysis
# - Correlation matrix
# - Heatmap
```

## Part 5: Multivariate Analysis

```python
# TODO: Survival by Pclass and Sex
# - Grouped bar chart
# - Facet grid

# TODO: Age, Fare, and Survival
# - 3D scatter plot
# - Pair plot

# TODO: Family size impact
# - Survival rate by family size
# - Interaction effects
```

## Part 6: Statistical Tests

```python
# TODO: Chi-square tests
# - Sex vs Survival
# - Pclass vs Survival

# TODO: T-tests
# - Age of survivors vs non-survivors
# - Fare of survivors vs non-survivors

# TODO: ANOVA
# - Age across Pclass groups
```

## Part 7: Visualization Dashboard

Create a comprehensive dashboard with:

```python
fig, axes = plt.subplots(3, 3, figsize=(20, 15))

# TODO: Plot 1 - Survival counts
# TODO: Plot 2 - Age distribution
# TODO: Plot 3 - Fare distribution
# TODO: Plot 4 - Survival by Sex
# TODO: Plot 5 - Survival by Pclass
# TODO: Plot 6 - Correlation heatmap
# TODO: Plot 7 - Family size distribution
# TODO: Plot 8 - Embarked port counts
# TODO: Plot 9 - Age vs Fare scatter

plt.tight_layout()
plt.savefig('titanic_dashboard.png', dpi=300)
```

## Part 8: Insights and Conclusions

Write a summary addressing:

1. **Key Findings:**
   - What factors most influenced survival?
   - Were there surprising patterns?
   - What about the data quality?

2. **Statistical Insights:**
   - Significant correlations
   - Group differences
   - Outliers and anomalies

3. **Recommendations:**
   - For feature engineering
   - For modeling
   - For further analysis

## Deliverables

1. **Jupyter Notebook** (`titanic_eda.ipynb`)
   - All code and analysis
   - Markdown explanations
   - Visualizations

2. **Report** (`titanic_report.md`)
   - Executive summary
   - Key findings
   - Visualizations
   - Conclusions

3. **Cleaned Dataset** (`titanic_cleaned.csv`)
   - Processed data
   - New features
   - Ready for modeling

## Evaluation Criteria

- **Data Cleaning (20%):** Proper handling of missing values
- **Exploration (30%):** Comprehensive analysis
- **Visualization (25%):** Clear, informative plots
- **Insights (15%):** Meaningful conclusions
- **Code Quality (10%):** Clean, documented code

## Bonus Challenges

1. **Interactive Dashboard:** Use Plotly for interactive plots
2. **Automated Report:** Generate PDF report with findings
3. **Feature Engineering:** Create 10+ new features
4. **Predictive Modeling:** Build a simple classifier
5. **Web App:** Deploy EDA as Streamlit app

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Kaggle Titanic Tutorial](https://www.kaggle.com/c/titanic)

## Example Code Structure

```python
# titanic_eda.py

class TitanicEDA:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
    
    def clean_data(self):
        """Clean and preprocess data."""
        pass
    
    def create_features(self):
        """Engineer new features."""
        pass
    
    def univariate_analysis(self):
        """Analyze individual features."""
        pass
    
    def bivariate_analysis(self):
        """Analyze feature relationships."""
        pass
    
    def visualize_dashboard(self):
        """Create visualization dashboard."""
        pass
    
    def generate_report(self):
        """Generate insights report."""
        pass

# Usage
eda = TitanicEDA('titanic_train.csv')
eda.clean_data()
eda.create_features()
eda.univariate_analysis()
eda.bivariate_analysis()
eda.visualize_dashboard()
eda.generate_report()
```

## Next Steps

After completing this project:
1. Compare your findings with Kaggle kernels
2. Try different visualization libraries (Plotly, Bokeh)
3. Build a predictive model (Week 4-5)
4. Deploy as a web application

Good luck! 🚢
