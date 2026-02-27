# Week 2 Resources: NumPy, Pandas & Matplotlib

## Official Documentation

### NumPy
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/index.html)
- [NumPy API Reference](https://numpy.org/doc/stable/reference/index.html)
- [NumPy for MATLAB Users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)

### Pandas
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cookbook](https://pandas.pydata.org/docs/user_guide/cookbook.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

### Matplotlib
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)

## Video Tutorials

### NumPy
1. **Keith Galli - Complete NumPy Tutorial**
   - Duration: 1 hour
   - Link: https://www.youtube.com/watch?v=GB9ByFAIAH4
   - Comprehensive beginner-friendly tutorial

2. **freeCodeCamp - NumPy Course**
   - Duration: 1.5 hours
   - Covers arrays, operations, broadcasting

### Pandas
1. **Corey Schafer - Pandas Tutorial Series**
   - Duration: ~6 hours (playlist)
   - Link: https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS
   - Excellent step-by-step guide

2. **Data School - Pandas Best Practices**
   - Duration: Various short videos
   - Link: https://www.youtube.com/user/dataschool
   - Tips and tricks

### Matplotlib/Seaborn
1. **Sentdex - Matplotlib Tutorial**
   - Duration: ~3 hours
   - Link: https://www.youtube.com/playlist?list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF
   - Comprehensive visualization guide

2. **Python Engineer - Seaborn Tutorial**
   - Duration: 30 minutes
   - Quick introduction to Seaborn

## Online Courses

1. **DataCamp - NumPy & Pandas**
   - Interactive exercises
   - Hands-on practice
   - Free intro courses

2. **Coursera - Applied Data Science with Python**
   - University of Michigan
   - Week 2 covers Pandas
   - Certificate available

3. **Kaggle Learn - Pandas**
   - Free micro-course
   - Practical exercises
   - Real datasets

## Books

### NumPy
1. **"Python for Data Analysis" by Wes McKinney**
   - Chapter 4: NumPy Basics
   - Written by Pandas creator
   - Practical focus

2. **"NumPy Beginner's Guide" by Ivan Idris**
   - Comprehensive introduction
   - Many examples

### Pandas
1. **"Python for Data Analysis" by Wes McKinney**
   - Chapters 5-10: Pandas in depth
   - Authoritative source
   - 3rd edition (2022) most recent

2. **"Pandas Cookbook" by Theodore Petrou**
   - Recipe-based learning
   - Practical solutions

### Visualization
1. **"Python Data Science Handbook" by Jake VanderPlas**
   - Chapter 4: Matplotlib
   - Free online version
   - Excellent resource

## Interactive Tutorials

1. **NumPy Exercises**
   - Link: https://github.com/rougier/numpy-100
   - 100 NumPy exercises
   - Solutions provided

2. **Pandas Exercises**
   - Link: https://github.com/guipsamora/pandas_exercises
   - Real datasets
   - Progressive difficulty

3. **Python Graph Gallery**
   - Link: https://python-graph-gallery.com/
   - Matplotlib/Seaborn examples
   - Copy-paste ready code

## Cheat Sheets

1. **NumPy Cheat Sheet**
   - [DataCamp NumPy](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
   - Quick reference for common operations

2. **Pandas Cheat Sheet**
   - [Pandas Official](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
   - [DataCamp Pandas](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python)

3. **Matplotlib Cheat Sheet**
   - [Official Cheatsheets](https://matplotlib.org/cheatsheets/)
   - Beginner and advanced versions

## Practice Datasets

### For Pandas Practice:
1. **Titanic Dataset**
   - Classic beginner dataset
   - Kaggle: https://www.kaggle.com/c/titanic

2. **Iris Dataset**
   - Simple classification dataset
   - Built into scikit-learn

3. **MovieLens**
   - Movie ratings dataset
   - Good for groupby operations

4. **NYC Taxi Data**
   - Time series practice
   - Large dataset

### Where to Find Datasets:
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Data.gov](https://www.data.gov/)

## Blogs & Articles

1. **Real Python - NumPy & Pandas**
   - High-quality tutorials
   - Link: https://realpython.com/

2. **Towards Data Science**
   - Many Pandas articles
   - Link: https://towardsdatascience.com/

3. **Chris Albon's Notes**
   - Quick code snippets
   - Link: https://chrisalbon.com/

## Communities

1. **Stack Overflow**
   - Tag: [numpy], [pandas], [matplotlib]
   - Search before asking

2. **Reddit**
   - r/learnpython
   - r/datascience
   - r/Python

3. **Discord**
   - Python Discord server
   - Data Science Discord

## Common Operations Quick Reference

### NumPy
```python
# Array creation
np.array([1, 2, 3])
np.zeros((3, 4))
np.arange(0, 10, 2)
np.linspace(0, 1, 5)

# Operations
arr.reshape(3, 4)
arr.T  # Transpose
arr @ arr2  # Matrix multiplication
np.sum(arr, axis=0)

# Indexing
arr[arr > 5]  # Boolean indexing
arr[[0, 2, 4]]  # Fancy indexing
```

### Pandas
```python
# Reading data
pd.read_csv('file.csv')
pd.read_excel('file.xlsx')

# Exploration
df.head()
df.info()
df.describe()

# Selection
df['column']
df[['col1', 'col2']]
df.loc[0:5, 'column']
df.iloc[0:5, 0:3]

# Filtering
df[df['age'] > 30]
df.query('age > 30 and city == "NYC"')

# Grouping
df.groupby('category').mean()
df.groupby(['cat1', 'cat2']).agg({'col': ['mean', 'sum']})

# Merging
pd.merge(df1, df2, on='key')
pd.concat([df1, df2], axis=0)
```

### Matplotlib
```python
# Basic plot
plt.plot(x, y)
plt.scatter(x, y)
plt.hist(data)
plt.bar(categories, values)

# Customization
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.legend()
plt.grid(True)

# Subplots
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(x, y)
```

## Performance Tips

### NumPy
- Use vectorization instead of loops
- Avoid copying arrays unnecessarily
- Use views instead of copies when possible
- Specify dtype to save memory

### Pandas
- Use categorical dtype for strings
- Read only needed columns: `usecols`
- Use chunking for large files
- Avoid iterrows(), use vectorized operations

## Troubleshooting

### Common Errors:
1. **ValueError: shapes not aligned**
   - Check array dimensions
   - Use .reshape() or broadcasting

2. **KeyError: 'column'**
   - Column name doesn't exist
   - Check df.columns

3. **SettingWithCopyWarning**
   - Use .loc[] or .copy()
   - Avoid chained assignment

## Next Steps

After mastering this week:
1. Practice on Kaggle datasets
2. Create your own visualizations
3. Combine NumPy/Pandas for data pipelines
4. Move to Week 3: Statistics

## Recommended Learning Path

1. **Day 1-2:** NumPy fundamentals
   - Arrays, indexing, operations
   - Complete 01_numpy_fundamentals.ipynb

2. **Day 3-4:** Pandas basics
   - DataFrames, selection, filtering
   - Complete 02_pandas_data_manipulation.ipynb

3. **Day 5-6:** Visualization
   - Matplotlib and Seaborn
   - Complete 03_data_visualization.ipynb

4. **Day 7:** Mini Project
   - Titanic EDA
   - Apply all concepts

---

**Happy Learning! 📚**
