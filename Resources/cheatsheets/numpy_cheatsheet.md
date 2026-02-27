# NumPy Cheat Sheet

## Array Creation

```python
import numpy as np

# From lists
np.array([1, 2, 3])
np.array([[1, 2], [3, 4]])

# Special arrays
np.zeros((3, 4))          # 3x4 array of zeros
np.ones((2, 3))           # 2x3 array of ones
np.empty((2, 2))          # Uninitialized 2x2
np.full((3, 3), 7)        # 3x3 filled with 7
np.eye(4)                 # 4x4 identity matrix

# Ranges
np.arange(0, 10, 2)       # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)      # 5 evenly spaced values from 0 to 1
np.logspace(0, 2, 5)      # 5 values from 10^0 to 10^2

# Random
np.random.rand(3, 3)      # Uniform [0, 1)
np.random.randn(3, 3)     # Standard normal
np.random.randint(0, 10, (3, 3))  # Random integers
np.random.choice([1,2,3], size=10)  # Random choice
```

## Array Properties

```python
arr.shape          # Dimensions (rows, cols)
arr.ndim           # Number of dimensions
arr.size           # Total number of elements
arr.dtype          # Data type
arr.itemsize       # Size of each element in bytes
arr.nbytes         # Total bytes consumed
```

## Indexing & Slicing

```python
# Basic indexing
arr[0]             # First element
arr[-1]            # Last element
arr[1:4]           # Elements 1 to 3
arr[::2]           # Every other element
arr[::-1]          # Reverse array

# 2D indexing
arr[1, 2]          # Element at row 1, col 2
arr[0, :]          # First row
arr[:, 1]          # Second column
arr[0:2, 1:3]      # Subarray

# Boolean indexing
arr[arr > 5]       # Elements greater than 5
arr[(arr > 2) & (arr < 8)]  # Multiple conditions

# Fancy indexing
arr[[0, 2, 4]]     # Select specific indices
arr[[0, 2], [1, 3]]  # Select (0,1) and (2,3)
```

## Array Operations

```python
# Element-wise operations
a + b              # Addition
a - b              # Subtraction
a * b              # Multiplication
a / b              # Division
a ** 2             # Power
a % 2              # Modulo

# Universal functions
np.sqrt(a)         # Square root
np.exp(a)          # Exponential
np.log(a)          # Natural log
np.sin(a)          # Sine
np.cos(a)          # Cosine
np.abs(a)          # Absolute value

# Comparison
a == b             # Element-wise equality
a > 5              # Element-wise comparison
np.allclose(a, b)  # Check if arrays are close
```

## Aggregation Functions

```python
np.sum(arr)        # Sum of all elements
np.sum(arr, axis=0)  # Sum along axis 0 (columns)
np.sum(arr, axis=1)  # Sum along axis 1 (rows)

np.mean(arr)       # Mean
np.median(arr)     # Median
np.std(arr)        # Standard deviation
np.var(arr)        # Variance
np.min(arr)        # Minimum
np.max(arr)        # Maximum

np.argmin(arr)     # Index of minimum
np.argmax(arr)     # Index of maximum

np.cumsum(arr)     # Cumulative sum
np.cumprod(arr)    # Cumulative product
```

## Matrix Operations

```python
# Matrix multiplication
A @ B              # Matrix multiplication (Python 3.5+)
np.dot(A, B)       # Matrix multiplication
A * B              # Element-wise multiplication

# Transpose
A.T                # Transpose
np.transpose(A)    # Transpose

# Linear algebra
np.linalg.inv(A)   # Inverse
np.linalg.det(A)   # Determinant
np.linalg.eig(A)   # Eigenvalues and eigenvectors
np.linalg.svd(A)   # Singular value decomposition
np.linalg.solve(A, b)  # Solve Ax = b
np.trace(A)        # Trace (sum of diagonal)
```

## Reshaping

```python
arr.reshape(3, 4)  # Reshape to 3x4
arr.flatten()      # Flatten to 1D
arr.ravel()        # Flatten (returns view if possible)
arr.T              # Transpose

# Add/remove dimensions
arr[np.newaxis, :]  # Add dimension at start
arr[:, np.newaxis]  # Add dimension at end
np.expand_dims(arr, axis=0)  # Add dimension
np.squeeze(arr)    # Remove single-dimensional entries
```

## Stacking & Splitting

```python
# Stacking
np.vstack([a, b])  # Vertical stack (rows)
np.hstack([a, b])  # Horizontal stack (columns)
np.dstack([a, b])  # Depth stack
np.concatenate([a, b], axis=0)  # Concatenate

# Splitting
np.split(arr, 3)   # Split into 3 equal parts
np.hsplit(arr, 3)  # Horizontal split
np.vsplit(arr, 3)  # Vertical split
```

## Broadcasting

```python
# Broadcasting allows operations on arrays of different shapes
a = np.array([[1, 2, 3],
              [4, 5, 6]])  # Shape: (2, 3)
b = np.array([10, 20, 30])  # Shape: (3,)

c = a + b  # b is broadcasted to (2, 3)
# Result: [[11, 22, 33],
#          [14, 25, 36]]

# Broadcasting rules:
# 1. If arrays have different number of dimensions, 
#    prepend 1s to the smaller shape
# 2. Arrays are compatible if dimensions are equal or one is 1
# 3. After broadcasting, each array behaves as if it had the larger shape
```

## Useful Functions

```python
# Sorting
np.sort(arr)       # Sort array
np.argsort(arr)    # Indices that would sort array
np.sort(arr, axis=0)  # Sort along axis

# Unique
np.unique(arr)     # Unique elements
np.unique(arr, return_counts=True)  # With counts

# Set operations
np.intersect1d(a, b)  # Intersection
np.union1d(a, b)      # Union
np.setdiff1d(a, b)    # Difference

# Conditions
np.where(arr > 5, 1, 0)  # If arr > 5, return 1, else 0
np.select([cond1, cond2], [val1, val2], default=0)

# Clipping
np.clip(arr, 0, 10)  # Clip values to [0, 10]

# NaN handling
np.isnan(arr)      # Check for NaN
np.nanmean(arr)    # Mean ignoring NaN
np.nansum(arr)     # Sum ignoring NaN
```

## Performance Tips

```python
# Use vectorization instead of loops
# Bad:
result = []
for i in range(len(arr)):
    result.append(arr[i] * 2)

# Good:
result = arr * 2

# Use views instead of copies when possible
view = arr[1:5]    # View (shares memory)
copy = arr[1:5].copy()  # Copy (new memory)

# Specify dtype to save memory
arr = np.array([1, 2, 3], dtype=np.int8)  # 8-bit integers

# Use in-place operations
arr += 1           # In-place addition
arr *= 2           # In-place multiplication
```

## Common Patterns

```python
# Normalize array (z-score)
normalized = (arr - np.mean(arr)) / np.std(arr)

# Min-max scaling
scaled = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

# Euclidean distance
dist = np.sqrt(np.sum((a - b) ** 2))

# Cosine similarity
similarity = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# One-hot encoding
def one_hot(arr, num_classes):
    return np.eye(num_classes)[arr]

# Softmax
def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)
```

## Saving & Loading

```python
# Save/load single array
np.save('array.npy', arr)
arr = np.load('array.npy')

# Save/load multiple arrays
np.savez('arrays.npz', a=arr1, b=arr2)
data = np.load('arrays.npz')
arr1 = data['a']
arr2 = data['b']

# Save/load text
np.savetxt('array.txt', arr)
arr = np.loadtxt('array.txt')

# Save/load CSV
np.savetxt('array.csv', arr, delimiter=',')
arr = np.loadtxt('array.csv', delimiter=',')
```

## Random Number Generation

```python
# Set seed for reproducibility
np.random.seed(42)

# Random integers
np.random.randint(0, 10, size=5)

# Random floats
np.random.rand(3, 3)        # Uniform [0, 1)
np.random.random((3, 3))    # Uniform [0, 1)
np.random.uniform(0, 10, 5) # Uniform [0, 10)

# Random normal
np.random.randn(3, 3)       # Standard normal (μ=0, σ=1)
np.random.normal(5, 2, 100) # Normal (μ=5, σ=2)

# Random choice
np.random.choice([1, 2, 3, 4, 5], size=10, replace=True)
np.random.choice(arr, size=5, replace=False, p=[0.1, 0.2, 0.7])

# Shuffle
np.random.shuffle(arr)      # In-place shuffle
np.random.permutation(arr)  # Return shuffled copy
```

---

**Quick Reference:** Keep this handy while coding!
