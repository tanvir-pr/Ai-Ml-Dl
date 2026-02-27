# Week 1 Exercises: Python & Math Basics

## Instructions
- Complete these exercises to reinforce your learning
- Try to solve them without looking at solutions first
- Solutions are provided at the end of each section
- Time estimate: 3-4 hours

---

## Part 1: Python Programming (5 exercises)

### Exercise 1.1: Data Statistics Calculator
Write a function `calculate_stats(numbers)` that takes a list of numbers and returns a dictionary with:
- `mean`: average value
- `median`: middle value
- `std`: standard deviation
- `min`: minimum value
- `max`: maximum value

```python
# Example usage:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats = calculate_stats(data)
# Expected: {'mean': 5.5, 'median': 5.5, 'std': 2.87, 'min': 1, 'max': 10}
```

### Exercise 1.2: Feature Scaler Class
Create a `StandardScaler` class that:
- Has a `fit(X)` method to compute mean and std from training data
- Has a `transform(X)` method to normalize data: `(X - mean) / std`
- Has a `fit_transform(X)` method that does both

```python
# Example usage:
scaler = StandardScaler()
X_train = [[1, 2], [3, 4], [5, 6]]
X_test = [[7, 8]]
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Exercise 1.3: Batch Generator
Implement a generator function `batch_generator(data, labels, batch_size)` that yields batches of data.

```python
# Example usage:
X = list(range(100))
y = list(range(100))
for batch_X, batch_y in batch_generator(X, y, batch_size=10):
    print(f"Batch shape: {len(batch_X)}")
    # Process batch...
```

### Exercise 1.4: Model Pipeline
Create a `Pipeline` class that chains multiple transformations and a model:
- Constructor takes list of (name, transformer/model) tuples
- `fit(X, y)` method fits all components
- `predict(X)` method applies all transformations and final prediction

```python
# Example usage:
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

### Exercise 1.5: Cache Decorator
Write a `cache_results` decorator that caches function results based on input arguments.

```python
@cache_results
def expensive_computation(x, y):
    time.sleep(1)  # Simulate expensive operation
    return x ** y

# First call: takes 1 second
result1 = expensive_computation(2, 10)
# Second call with same args: instant (cached)
result2 = expensive_computation(2, 10)
```

---

## Part 2: Linear Algebra (5 exercises)

### Exercise 2.1: Matrix Multiplication from Scratch
Implement matrix multiplication without using NumPy's matmul or @ operator.

```python
def matrix_multiply(A, B):
    """
    Multiply two matrices A (m x n) and B (n x p).
    Returns C (m x p) where C[i][j] = sum(A[i][k] * B[k][j])
    """
    # Your code here
    pass

# Test
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = matrix_multiply(A, B)
# Expected: [[19, 22], [43, 50]]
```

### Exercise 2.2: Vector Projection
Compute the projection of vector `a` onto vector `b`.

Formula: $\text{proj}_b(a) = \frac{a \cdot b}{b \cdot b} b$

```python
def vector_projection(a, b):
    """Project vector a onto vector b."""
    # Your code here
    pass

# Test
a = np.array([3, 4])
b = np.array([1, 0])
proj = vector_projection(a, b)
# Expected: [3, 0]
```

### Exercise 2.3: Gram-Schmidt Orthogonalization
Implement the Gram-Schmidt process to orthogonalize a set of vectors.

```python
def gram_schmidt(vectors):
    """
    Orthogonalize a list of vectors using Gram-Schmidt process.
    Returns list of orthonormal vectors.
    """
    # Your code here
    pass

# Test
vectors = [np.array([1, 1, 0]), 
           np.array([1, 0, 1]),
           np.array([0, 1, 1])]
orthonormal = gram_schmidt(vectors)
```

### Exercise 2.4: Matrix Rank
Compute the rank of a matrix using SVD (number of non-zero singular values).

```python
def matrix_rank(A, tolerance=1e-10):
    """Compute rank of matrix A."""
    # Your code here
    pass

# Test
A = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
rank = matrix_rank(A)
# Expected: 1 (all rows are linearly dependent)
```

### Exercise 2.5: Image Compression with SVD
Use SVD to compress an image by keeping only the top k singular values.

```python
def compress_image(image, k):
    """
    Compress image using SVD by keeping top k singular values.
    Returns compressed image and compression ratio.
    """
    # Your code here
    pass

# Test with a grayscale image
# Calculate compression ratio: (original_size / compressed_size)
```

---

## Part 3: Calculus (5 exercises)

### Exercise 3.1: Numerical Gradient Checker
Implement a gradient checker to verify analytical gradients.

```python
def check_gradient(f, grad_f, x, epsilon=1e-5):
    """
    Check if analytical gradient matches numerical gradient.
    Returns True if error is below threshold.
    """
    # Your code here
    pass

# Test
f = lambda x: np.sum(x**2)
grad_f = lambda x: 2*x
x = np.array([1.0, 2.0, 3.0])
is_correct = check_gradient(f, grad_f, x)
```

### Exercise 3.2: Newton's Method
Implement Newton's method for finding roots: $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$

```python
def newtons_method(f, f_prime, x0, tolerance=1e-6, max_iter=100):
    """Find root of f using Newton's method."""
    # Your code here
    pass

# Test: Find root of f(x) = x^2 - 2 (should give sqrt(2))
f = lambda x: x**2 - 2
f_prime = lambda x: 2*x
root = newtons_method(f, f_prime, x0=1.0)
# Expected: ~1.414
```

### Exercise 3.3: Gradient Descent with Momentum
Implement gradient descent with momentum:
- $v_t = \beta v_{t-1} + (1-\beta) \nabla f(x_t)$
- $x_{t+1} = x_t - \alpha v_t$

```python
def gradient_descent_momentum(f, grad_f, x0, learning_rate=0.1, 
                              beta=0.9, n_iterations=100):
    """Gradient descent with momentum."""
    # Your code here
    pass
```

### Exercise 3.4: Finite Difference Methods
Implement forward, backward, and central difference methods for derivatives.

```python
def forward_difference(f, x, h=1e-5):
    """f'(x) ≈ (f(x+h) - f(x)) / h"""
    pass

def backward_difference(f, x, h=1e-5):
    """f'(x) ≈ (f(x) - f(x-h)) / h"""
    pass

def central_difference(f, x, h=1e-5):
    """f'(x) ≈ (f(x+h) - f(x-h)) / (2h)"""
    pass

# Compare accuracy of all three methods
```

### Exercise 3.5: Automatic Differentiation (Simple)
Implement a simple automatic differentiation system for scalar functions.

```python
class Variable:
    """Variable with value and gradient."""
    def __init__(self, value):
        self.value = value
        self.grad = 0
    
    def __add__(self, other):
        # Implement addition with gradient tracking
        pass
    
    def __mul__(self, other):
        # Implement multiplication with gradient tracking
        pass

# Test
x = Variable(2.0)
y = Variable(3.0)
z = x * y + x
# z.backward() should compute gradients
```

---

## Solutions

<details>
<summary>Click to reveal solutions</summary>

### Solution 1.1: Data Statistics Calculator

```python
import math

def calculate_stats(numbers):
    """Calculate statistics for a list of numbers."""
    n = len(numbers)
    
    # Mean
    mean = sum(numbers) / n
    
    # Median
    sorted_nums = sorted(numbers)
    if n % 2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    # Standard deviation
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std = math.sqrt(variance)
    
    # Min and max
    min_val = min(numbers)
    max_val = max(numbers)
    
    return {
        'mean': mean,
        'median': median,
        'std': std,
        'min': min_val,
        'max': max_val
    }
```

### Solution 1.2: Feature Scaler Class

```python
import numpy as np

class StandardScaler:
    """Standardize features by removing mean and scaling to unit variance."""
    
    def __init__(self):
        self.mean_ = None
        self.std_ = None
    
    def fit(self, X):
        """Compute mean and std from training data."""
        X = np.array(X)
        self.mean_ = np.mean(X, axis=0)
        self.std_ = np.std(X, axis=0)
        return self
    
    def transform(self, X):
        """Transform data using computed statistics."""
        if self.mean_ is None or self.std_ is None:
            raise ValueError("Scaler must be fitted before transform")
        X = np.array(X)
        return (X - self.mean_) / (self.std_ + 1e-8)
    
    def fit_transform(self, X):
        """Fit and transform in one step."""
        return self.fit(X).transform(X)
```

### Solution 1.3: Batch Generator

```python
def batch_generator(data, labels, batch_size):
    """Generate batches of data and labels."""
    n_samples = len(data)
    indices = list(range(n_samples))
    
    for start_idx in range(0, n_samples, batch_size):
        end_idx = min(start_idx + batch_size, n_samples)
        batch_indices = indices[start_idx:end_idx]
        
        batch_data = [data[i] for i in batch_indices]
        batch_labels = [labels[i] for i in batch_indices]
        
        yield batch_data, batch_labels
```

### Solution 1.4: Model Pipeline

```python
class Pipeline:
    """Chain multiple transformations and a model."""
    
    def __init__(self, steps):
        """
        steps: list of (name, transformer/model) tuples
        """
        self.steps = steps
    
    def fit(self, X, y):
        """Fit all components."""
        X_transformed = X
        
        # Fit all transformers
        for name, transformer in self.steps[:-1]:
            X_transformed = transformer.fit_transform(X_transformed)
        
        # Fit final model
        name, model = self.steps[-1]
        model.fit(X_transformed, y)
        
        return self
    
    def predict(self, X):
        """Apply all transformations and predict."""
        X_transformed = X
        
        # Apply all transformers
        for name, transformer in self.steps[:-1]:
            X_transformed = transformer.transform(X_transformed)
        
        # Predict with final model
        name, model = self.steps[-1]
        return model.predict(X_transformed)
```

### Solution 1.5: Cache Decorator

```python
def cache_results(func):
    """Decorator to cache function results."""
    cache = {}
    
    def wrapper(*args, **kwargs):
        # Create cache key from arguments
        key = (args, tuple(sorted(kwargs.items())))
        
        if key in cache:
            print("Returning cached result")
            return cache[key]
        
        # Compute result
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper
```

### Solution 2.1: Matrix Multiplication

```python
def matrix_multiply(A, B):
    """Multiply matrices A and B."""
    m, n = len(A), len(A[0])
    n2, p = len(B), len(B[0])
    
    if n != n2:
        raise ValueError(f"Incompatible dimensions: ({m}x{n}) and ({n2}x{p})")
    
    # Initialize result matrix
    C = [[0 for _ in range(p)] for _ in range(m)]
    
    # Compute each element
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C
```

### Solution 2.2: Vector Projection

```python
def vector_projection(a, b):
    """Project vector a onto vector b."""
    a = np.array(a)
    b = np.array(b)
    
    # proj_b(a) = (a·b / b·b) * b
    dot_ab = np.dot(a, b)
    dot_bb = np.dot(b, b)
    
    return (dot_ab / dot_bb) * b
```

### Solution 2.3: Gram-Schmidt Orthogonalization

```python
def gram_schmidt(vectors):
    """Orthogonalize vectors using Gram-Schmidt process."""
    orthonormal = []
    
    for v in vectors:
        # Subtract projections onto all previous orthonormal vectors
        u = v.copy()
        for basis in orthonormal:
            u = u - vector_projection(v, basis)
        
        # Normalize
        u = u / np.linalg.norm(u)
        orthonormal.append(u)
    
    return orthonormal
```

### Solution 2.4: Matrix Rank

```python
def matrix_rank(A, tolerance=1e-10):
    """Compute rank of matrix using SVD."""
    U, S, VT = np.linalg.svd(A)
    # Count singular values above tolerance
    return np.sum(S > tolerance)
```

### Solution 2.5: Image Compression with SVD

```python
def compress_image(image, k):
    """Compress image using SVD."""
    # Perform SVD
    U, S, VT = np.linalg.svd(image, full_matrices=False)
    
    # Keep only top k singular values
    U_k = U[:, :k]
    S_k = S[:k]
    VT_k = VT[:k, :]
    
    # Reconstruct
    compressed = U_k @ np.diag(S_k) @ VT_k
    
    # Calculate compression ratio
    original_size = image.shape[0] * image.shape[1]
    compressed_size = k * (image.shape[0] + image.shape[1] + 1)
    compression_ratio = original_size / compressed_size
    
    return compressed, compression_ratio
```

### Solution 3.1: Numerical Gradient Checker

```python
def check_gradient(f, grad_f, x, epsilon=1e-5, threshold=1e-5):
    """Check if analytical gradient matches numerical gradient."""
    analytical_grad = grad_f(x)
    numerical_grad = np.zeros_like(x)
    
    # Compute numerical gradient
    for i in range(len(x)):
        x_plus = x.copy()
        x_plus[i] += epsilon
        x_minus = x.copy()
        x_minus[i] -= epsilon
        
        numerical_grad[i] = (f(x_plus) - f(x_minus)) / (2 * epsilon)
    
    # Compute relative error
    error = np.linalg.norm(analytical_grad - numerical_grad)
    relative_error = error / (np.linalg.norm(analytical_grad) + np.linalg.norm(numerical_grad))
    
    print(f"Analytical: {analytical_grad}")
    print(f"Numerical: {numerical_grad}")
    print(f"Relative error: {relative_error}")
    
    return relative_error < threshold
```

### Solution 3.2: Newton's Method

```python
def newtons_method(f, f_prime, x0, tolerance=1e-6, max_iter=100):
    """Find root using Newton's method."""
    x = x0
    
    for i in range(max_iter):
        fx = f(x)
        
        if abs(fx) < tolerance:
            print(f"Converged after {i+1} iterations")
            return x
        
        fpx = f_prime(x)
        if abs(fpx) < 1e-12:
            raise ValueError("Derivative too close to zero")
        
        x = x - fx / fpx
    
    print(f"Did not converge after {max_iter} iterations")
    return x
```

### Solution 3.3: Gradient Descent with Momentum

```python
def gradient_descent_momentum(f, grad_f, x0, learning_rate=0.1, 
                              beta=0.9, n_iterations=100):
    """Gradient descent with momentum."""
    x = x0.copy()
    v = np.zeros_like(x)
    history = [x.copy()]
    
    for i in range(n_iterations):
        grad = grad_f(x)
        
        # Update velocity
        v = beta * v + (1 - beta) * grad
        
        # Update position
        x = x - learning_rate * v
        history.append(x.copy())
    
    return x, np.array(history)
```

### Solution 3.4: Finite Difference Methods

```python
def forward_difference(f, x, h=1e-5):
    """Forward difference approximation."""
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h=1e-5):
    """Backward difference approximation."""
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h=1e-5):
    """Central difference approximation (more accurate)."""
    return (f(x + h) - f(x - h)) / (2 * h)

# Compare accuracy
f = lambda x: x**3
f_prime = lambda x: 3*x**2

x = 2.0
true_derivative = f_prime(x)

print(f"True derivative: {true_derivative}")
print(f"Forward difference: {forward_difference(f, x)}")
print(f"Backward difference: {backward_difference(f, x)}")
print(f"Central difference: {central_difference(f, x)}")
```

</details>

---

## Additional Challenge Problems

1. **Eigenface**: Implement PCA-based face recognition
2. **Gradient Visualization**: Create animated gradient descent visualization
3. **Numerical Integration**: Implement trapezoidal and Simpson's rule
4. **Jacobian Matrix**: Compute Jacobian for vector-valued functions
5. **Hessian Matrix**: Compute second-order derivatives for optimization

## Resources
- [NumPy Documentation](https://numpy.org/doc/)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Khan Academy: Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [3Blue1Brown: Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
