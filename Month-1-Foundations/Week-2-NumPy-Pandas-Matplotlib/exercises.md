# Week 2 Exercises: NumPy, Pandas & Matplotlib

## NumPy Exercises (10 problems)

### Exercise 2.1: Array Manipulation
Create a function that takes a 2D array and returns:
- Row-wise mean
- Column-wise standard deviation
- Flattened array sorted in descending order

### Exercise 2.2: Broadcasting Challenge
Normalize a dataset (100 samples, 5 features) using broadcasting.
Compute: `(X - mean) / std` for each feature.

### Exercise 2.3: Vectorized Distance
Implement cosine similarity between all pairs of vectors in a matrix without loops.

### Exercise 2.4: Image Operations
Create a 28x28 random "image" and:
- Add Gaussian noise
- Apply a 3x3 averaging filter
- Rotate by 90 degrees

### Exercise 2.5: Performance Comparison
Compare loop vs vectorized implementation for:
- Element-wise square root
- Matrix-vector multiplication
- Conditional selection

## Pandas Exercises (10 problems)

### Exercise 2.6: Data Loading
Load a CSV file and:
- Display first/last 10 rows
- Show data types and missing values
- Generate summary statistics

### Exercise 2.7: Data Cleaning
Handle missing data using:
- Forward fill
- Backward fill
- Mean/median imputation
- Drop rows/columns

### Exercise 2.8: GroupBy Operations
Group data by category and compute:
- Mean, median, std per group
- Custom aggregation functions
- Multiple aggregations at once

### Exercise 2.9: Time Series
Create a date range and:
- Resample to different frequencies
- Compute rolling statistics
- Handle time zones

### Exercise 2.10: Merging DataFrames
Merge two datasets using:
- Inner join
- Left join
- Outer join
- Concatenation

## Matplotlib Exercises (5 problems)

### Exercise 2.11: Multiple Plots
Create a 2x2 subplot grid with:
- Line plot
- Scatter plot
- Histogram
- Bar chart

### Exercise 2.12: Customization
Create a publication-quality plot with:
- Custom colors and styles
- Legends and labels
- Grid and annotations
- Proper sizing

### Exercise 2.13: 3D Visualization
Plot a 3D surface and scatter plot.

### Exercise 2.14: Heatmap
Create a correlation heatmap with annotations.

### Exercise 2.15: Animation
Create an animated plot showing data evolution.

## Solutions

<details>
<summary>Click to reveal solutions</summary>

### Solution 2.1
```python
def array_stats(arr):
    row_mean = np.mean(arr, axis=1)
    col_std = np.std(arr, axis=0)
    flat_sorted = np.sort(arr.flatten())[::-1]
    return row_mean, col_std, flat_sorted
```

### Solution 2.2
```python
def normalize_dataset(X):
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std
```

### Solution 2.3
```python
def cosine_similarity_matrix(X):
    # Normalize rows
    X_norm = X / np.linalg.norm(X, axis=1, keepdims=True)
    # Compute similarity
    return X_norm @ X_norm.T
```

</details>

## Additional Challenges
1. Implement k-NN from scratch using NumPy
2. Create a data pipeline with Pandas
3. Build an interactive dashboard with Plotly
