# Mini Project: Matrix Calculator and Linear Algebra Library

## Project Overview
Build a comprehensive matrix calculator from scratch that implements core linear algebra operations. This project will solidify your understanding of both Python programming and linear algebra concepts.

**Time estimate:** 4-6 hours  
**Difficulty:** Intermediate  
**Learning goals:**
- Implement mathematical operations from first principles
- Practice object-oriented programming
- Understand computational complexity
- Build reusable library code

---

## Project Requirements

### Part 1: Matrix Class (Core Implementation)

Create a `Matrix` class with the following features:

#### 1.1 Constructor and Basic Properties
```python
class Matrix:
    def __init__(self, data):
        """
        Initialize matrix from 2D list.
        Example: Matrix([[1, 2], [3, 4]])
        """
        pass
    
    @property
    def shape(self):
        """Return (rows, cols) tuple."""
        pass
    
    def __repr__(self):
        """Pretty print the matrix."""
        pass
```

#### 1.2 Basic Operations
Implement these magic methods:
- `__add__(self, other)` - Matrix addition
- `__sub__(self, other)` - Matrix subtraction
- `__mul__(self, other)` - Scalar multiplication
- `__matmul__(self, other)` - Matrix multiplication (@ operator)
- `__getitem__(self, key)` - Access elements with `matrix[i, j]`
- `__setitem__(self, key, value)` - Set elements

#### 1.3 Matrix Operations
```python
def transpose(self):
    """Return transposed matrix."""
    pass

def determinant(self):
    """Compute determinant (for square matrices)."""
    pass

def inverse(self):
    """Compute matrix inverse."""
    pass

def trace(self):
    """Sum of diagonal elements."""
    pass
```

#### 1.4 Factory Methods
```python
@staticmethod
def zeros(rows, cols):
    """Create matrix of zeros."""
    pass

@staticmethod
def ones(rows, cols):
    """Create matrix of ones."""
    pass

@staticmethod
def identity(n):
    """Create n×n identity matrix."""
    pass

@staticmethod
def random(rows, cols, low=0, high=1):
    """Create matrix with random values."""
    pass
```

### Part 2: Vector Class

Create a `Vector` class that inherits from or works with Matrix:

```python
class Vector:
    def __init__(self, data):
        """Initialize from list."""
        pass
    
    def dot(self, other):
        """Dot product."""
        pass
    
    def norm(self, p=2):
        """Compute Lp norm."""
        pass
    
    def normalize(self):
        """Return unit vector."""
        pass
    
    def angle(self, other):
        """Angle between vectors (in radians)."""
        pass
```

### Part 3: Advanced Operations

Implement these advanced functions:

```python
def solve_linear_system(A, b):
    """
    Solve Ax = b using Gaussian elimination.
    Returns solution vector x.
    """
    pass

def eigenvalues(A, max_iter=1000):
    """
    Compute eigenvalues using QR algorithm.
    Returns list of eigenvalues.
    """
    pass

def svd(A):
    """
    Singular Value Decomposition.
    Returns U, S, VT such that A = U @ S @ VT
    """
    pass

def qr_decomposition(A):
    """
    QR decomposition using Gram-Schmidt.
    Returns Q (orthogonal) and R (upper triangular).
    """
    pass
```

### Part 4: Applications

Implement these practical applications:

```python
def least_squares(X, y):
    """
    Solve least squares problem: min ||Xw - y||^2
    Returns optimal weights w.
    """
    pass

def pca(X, n_components):
    """
    Principal Component Analysis.
    Returns transformed data and principal components.
    """
    pass

def gram_schmidt(vectors):
    """
    Orthogonalize list of vectors.
    Returns orthonormal basis.
    """
    pass
```

---

## Implementation Guide

### Step 1: Basic Matrix Class (1 hour)
Start with constructor, shape, and `__repr__`:

```python
class Matrix:
    def __init__(self, data):
        self.data = [row[:] for row in data]  # Deep copy
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
        self._validate()
    
    def _validate(self):
        """Ensure all rows have same length."""
        if not all(len(row) == self.cols for row in self.data):
            raise ValueError("All rows must have same length")
    
    @property
    def shape(self):
        return (self.rows, self.cols)
    
    def __repr__(self):
        return '\n'.join([' '.join([f'{val:8.3f}' for val in row]) 
                         for row in self.data])
```

### Step 2: Arithmetic Operations (1 hour)
Implement addition, subtraction, and multiplication:

```python
def __add__(self, other):
    if self.shape != other.shape:
        raise ValueError("Matrices must have same shape")
    
    result = []
    for i in range(self.rows):
        row = []
        for j in range(self.cols):
            row.append(self.data[i][j] + other.data[i][j])
        result.append(row)
    
    return Matrix(result)
```

### Step 3: Matrix Multiplication (1 hour)
Implement the @ operator:

```python
def __matmul__(self, other):
    if self.cols != other.rows:
        raise ValueError(f"Cannot multiply {self.shape} and {other.shape}")
    
    result = []
    for i in range(self.rows):
        row = []
        for j in range(other.cols):
            # Dot product of row i and column j
            val = sum(self.data[i][k] * other.data[k][j] 
                     for k in range(self.cols))
            row.append(val)
        result.append(row)
    
    return Matrix(result)
```

### Step 4: Determinant (Recursive) (1 hour)
Use cofactor expansion:

```python
def determinant(self):
    if self.rows != self.cols:
        raise ValueError("Determinant only for square matrices")
    
    if self.rows == 1:
        return self.data[0][0]
    
    if self.rows == 2:
        return (self.data[0][0] * self.data[1][1] - 
                self.data[0][1] * self.data[1][0])
    
    det = 0
    for j in range(self.cols):
        minor = self._get_minor(0, j)
        cofactor = ((-1) ** j) * self.data[0][j] * minor.determinant()
        det += cofactor
    
    return det

def _get_minor(self, row, col):
    """Get minor matrix by removing row and col."""
    minor_data = []
    for i in range(self.rows):
        if i == row:
            continue
        minor_row = []
        for j in range(self.cols):
            if j == col:
                continue
            minor_row.append(self.data[i][j])
        minor_data.append(minor_row)
    return Matrix(minor_data)
```

### Step 5: Testing (1 hour)
Create comprehensive tests:

```python
def test_matrix_operations():
    """Test suite for Matrix class."""
    
    # Test creation
    A = Matrix([[1, 2], [3, 4]])
    assert A.shape == (2, 2)
    
    # Test addition
    B = Matrix([[5, 6], [7, 8]])
    C = A + B
    assert C.data == [[6, 8], [10, 12]]
    
    # Test multiplication
    D = A @ B
    assert D.data == [[19, 22], [43, 50]]
    
    # Test transpose
    A_T = A.transpose()
    assert A_T.data == [[1, 3], [2, 4]]
    
    # Test determinant
    det_A = A.determinant()
    assert abs(det_A - (-2)) < 1e-10
    
    # Test identity
    I = Matrix.identity(3)
    assert I.data == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    
    print("All tests passed!")

test_matrix_operations()
```

---

## Deliverables

Create the following files:

1. **`matrix_lib.py`** - Main library with Matrix and Vector classes
2. **`test_matrix_lib.py`** - Comprehensive test suite
3. **`examples.py`** - Example usage and demonstrations
4. **`README.md`** - Documentation for your library
5. **`performance_analysis.ipynb`** - Jupyter notebook comparing your implementation with NumPy

---

## Example Usage

Your final library should work like this:

```python
from matrix_lib import Matrix, Vector, solve_linear_system, pca

# Create matrices
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

# Basic operations
C = A + B
D = A @ B
A_inv = A.inverse()

# Verify inverse
I = A @ A_inv
print(I)  # Should be close to identity

# Solve linear system
# 2x + 3y = 8
# 4x + y = 10
A = Matrix([[2, 3], [4, 1]])
b = Vector([8, 10])
x = solve_linear_system(A, b)
print(f"Solution: x = {x}")

# PCA example
data = Matrix.random(100, 5)  # 100 samples, 5 features
transformed, components = pca(data, n_components=2)
print(f"Reduced to 2 dimensions: {transformed.shape}")
```

---

## Bonus Challenges

1. **Performance Optimization**
   - Implement Strassen's algorithm for faster matrix multiplication
   - Use memoization for determinant calculation
   - Add parallel processing for large matrices

2. **Additional Features**
   - LU decomposition
   - Cholesky decomposition
   - Matrix exponential
   - Pseudoinverse (Moore-Penrose)

3. **Visualization**
   - Plot matrix transformations
   - Visualize eigenvalues/eigenvectors
   - Animate gradient descent on matrix functions

4. **Sparse Matrices**
   - Implement sparse matrix class
   - Use dictionary or COO format
   - Optimize for memory and speed

5. **GPU Acceleration**
   - Add optional GPU support using CuPy
   - Benchmark CPU vs GPU performance

---

## Evaluation Criteria

Your project will be evaluated on:

1. **Correctness** (40%)
   - All operations produce correct results
   - Edge cases handled properly
   - Comprehensive test coverage

2. **Code Quality** (30%)
   - Clean, readable code
   - Proper documentation
   - Good variable names
   - DRY principle followed

3. **Completeness** (20%)
   - All required features implemented
   - Examples provided
   - README documentation

4. **Performance** (10%)
   - Reasonable efficiency
   - No obvious bottlenecks
   - Comparison with NumPy

---

## Hints and Tips

1. **Start Simple**: Get basic operations working before advanced features
2. **Test Often**: Write tests as you implement features
3. **Use NumPy to Verify**: Compare your results with NumPy
4. **Handle Edge Cases**: Empty matrices, 1x1 matrices, non-square matrices
5. **Document**: Add docstrings to all methods
6. **Profile**: Use `time` or `cProfile` to find slow parts

---

## Resources

- [Matrix Multiplication Algorithm](https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm)
- [Gaussian Elimination](https://en.wikipedia.org/wiki/Gaussian_elimination)
- [QR Algorithm](https://en.wikipedia.org/wiki/QR_algorithm)
- [Gram-Schmidt Process](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process)

---

## Sample Test Cases

```python
# Test 1: Matrix multiplication
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[2, 0], [1, 2]])
C = A @ B
assert C.data == [[4, 4], [10, 8]]

# Test 2: Determinant
A = Matrix([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
det = A.determinant()
assert abs(det - (-306)) < 1e-10

# Test 3: Inverse
A = Matrix([[4, 7], [2, 6]])
A_inv = A.inverse()
I = A @ A_inv
# Check if I is close to identity
for i in range(2):
    for j in range(2):
        expected = 1 if i == j else 0
        assert abs(I.data[i][j] - expected) < 1e-10

# Test 4: Solve linear system
A = Matrix([[3, 2], [1, 2]])
b = Vector([7, 5])
x = solve_linear_system(A, b)
# Verify: A @ x ≈ b
result = A @ Matrix([[x.data[0]], [x.data[1]]])
assert abs(result.data[0][0] - 7) < 1e-10
assert abs(result.data[1][0] - 5) < 1e-10
```

---

## Submission Checklist

- [ ] Matrix class with all required methods
- [ ] Vector class implemented
- [ ] Advanced operations (solve, eigenvalues, SVD)
- [ ] Comprehensive test suite (>90% coverage)
- [ ] Example usage file
- [ ] README with documentation
- [ ] Performance comparison notebook
- [ ] All tests passing
- [ ] Code follows PEP 8 style guide

---

## Next Steps

After completing this project:
1. Compare your implementation with NumPy's source code
2. Read about BLAS (Basic Linear Algebra Subprograms)
3. Explore how production libraries optimize these operations
4. Move on to Week 2: NumPy and Pandas

Good luck! This project will give you deep understanding of linear algebra and Python programming.
