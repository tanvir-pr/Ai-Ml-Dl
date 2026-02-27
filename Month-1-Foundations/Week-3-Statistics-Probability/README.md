# Week 3: Statistics & Probability

## Overview
Master statistical concepts and probability theory essential for machine learning.

**Time Commitment:** 10-20 hours  
**Difficulty:** Intermediate  
**Prerequisites:** Week 1 (Math basics), Week 2 (NumPy, Pandas)

## Learning Objectives

By the end of this week, you will:
- Understand descriptive and inferential statistics
- Apply probability theory to ML problems
- Perform hypothesis testing
- Interpret statistical results
- Make data-driven decisions

## Week Structure

### Day 1-2: Descriptive Statistics
**Notebook:** `01_descriptive_statistics.ipynb`

**Topics:**
- Measures of central tendency (mean, median, mode)
- Measures of dispersion (variance, std, IQR)
- Distributions (normal, binomial, Poisson)
- Visualization techniques
- Outlier detection

**Practice:** 5 exercises on statistical measures

### Day 3-4: Probability Theory
**Notebook:** `02_probability_theory.ipynb`

**Topics:**
- Probability basics and rules
- Conditional probability
- Bayes' theorem
- Random variables
- Expectation and variance
- Common distributions

**Practice:** 5 exercises on probability

### Day 5-6: Hypothesis Testing
**Notebook:** `03_hypothesis_testing.ipynb`

**Topics:**
- Null and alternative hypotheses
- p-values and significance levels
- t-tests (one-sample, two-sample, paired)
- Chi-square tests
- ANOVA
- Confidence intervals
- Type I and Type II errors

**Practice:** 5 exercises on hypothesis testing

### Day 7: Mini Project
**Project:** A/B Test Analysis

Analyze an A/B test to determine if a new website design improves conversion rates.

## Content Status

### To Create:
- [ ] 01_descriptive_statistics.ipynb
- [ ] 02_probability_theory.ipynb
- [ ] 03_hypothesis_testing.ipynb
- [ ] exercises.md (15 problems)
- [ ] mini_project.md (A/B test analysis)
- [ ] resources.md

### Creation Guide:

**For Notebooks:**
1. Start with theory and formulas
2. Add NumPy/SciPy implementations
3. Include real data examples
4. Visualize distributions and results
5. Add practice problems

**Key Libraries:**
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
```

## Quick Start

### Option 1: Learn First, Create Content
1. Take a statistics course (Khan Academy, Coursera)
2. Follow along and create your own notebooks
3. Add examples that resonate with you
4. Document your learning

### Option 2: Use Existing Resources
1. Follow scikit-learn statistical tutorials
2. Adapt Kaggle notebooks
3. Use textbook examples
4. Customize for your needs

## Key Concepts

### Descriptive Statistics
- **Central Tendency:** Where is the center of the data?
- **Dispersion:** How spread out is the data?
- **Shape:** Is it symmetric? Skewed?

### Probability
- **P(A):** Probability of event A
- **P(A|B):** Probability of A given B
- **Bayes:** P(A|B) = P(B|A) × P(A) / P(B)

### Hypothesis Testing
- **H₀:** Null hypothesis (no effect)
- **H₁:** Alternative hypothesis (there is an effect)
- **p-value:** Probability of observing data if H₀ is true
- **α:** Significance level (usually 0.05)

## Real-World Applications

1. **A/B Testing:** Compare two versions
2. **Quality Control:** Detect defects
3. **Medical Trials:** Test drug effectiveness
4. **Marketing:** Analyze campaign performance
5. **Finance:** Risk assessment

## Resources

### Online Courses
- Khan Academy: Statistics & Probability
- Coursera: Statistics with Python
- edX: Probability and Statistics

### Books
- "Statistics for Machine Learning" by Jason Brownlee
- "Think Stats" by Allen Downey (free online)
- "Naked Statistics" by Charles Wheelan

### Videos
- StatQuest (YouTube) - Highly recommended!
- 3Blue1Brown - Bayes theorem
- Khan Academy - Full statistics course

### Interactive Tools
- Seeing Theory (https://seeing-theory.brown.edu/)
- Distribution Calculator
- Statistical Power Calculator

## Common Pitfalls

❌ Confusing correlation with causation  
❌ Misinterpreting p-values  
❌ Ignoring assumptions (normality, independence)  
❌ Cherry-picking significant results  
❌ Not checking for outliers  

✅ Always visualize your data first  
✅ Check assumptions before tests  
✅ Report effect sizes, not just p-values  
✅ Use appropriate tests for your data  
✅ Consider practical significance  

## Assessment

After completing this week, you should be able to:
- [ ] Calculate and interpret descriptive statistics
- [ ] Apply Bayes' theorem to real problems
- [ ] Perform and interpret t-tests
- [ ] Conduct chi-square tests
- [ ] Design and analyze A/B tests
- [ ] Make statistical inferences from data

## Next Week Preview

**Week 4: Linear Regression**
- Apply statistics to build predictive models
- Use hypothesis testing for feature selection
- Interpret regression coefficients statistically

## Tips for Success

1. **Practice with real data** - Use datasets from Kaggle
2. **Visualize everything** - Plots reveal patterns
3. **Understand assumptions** - Know when tests apply
4. **Connect to ML** - See how stats underlies ML
5. **Do the exercises** - Practice makes perfect

## Need Help?

- Cross Validated (Stack Exchange for statistics)
- r/statistics (Reddit)
- StatQuest videos
- Course forums

---

**Ready to dive into statistics? Let's go! 📊**
