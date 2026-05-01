# Complete ML/DL Topics — Main Explanation File

**Purpose:** Academic & job preparation reference. All topics with concise explanations.

**Course order (week by week):** [LEARNING_PATH.md](LEARNING_PATH.md)

---

## Quick Navigation
- [Math Topics](#math-topics)
- [Classical ML Topics](#classical-ml-topics)
- [Deep Learning Topics](#deep-learning-topics)
- [Book 1: Grokking Deep Learning](#book-1-grokking-deep-learning-by-andrew-w-trask)
- [Book 2: Deep Learning (Goodfellow et al.)](#book-2-deep-learning-by-goodfellow-bengio-courville)

---

# MATH TOPICS

## 1. Linear Algebra

| Topic | Explanation |
|-------|-------------|
| **Scalars, Vectors, Matrices** | Scalars are single numbers; vectors are 1D arrays; matrices are 2D arrays. Foundation for all ML data representation. |
| **Vector Addition** | Element-wise addition of two vectors. Used in gradient updates. |
| **Dot Product (Inner Product)** | Sum of element-wise products. Measures similarity; core of linear predictions: w·x + b. |
| **Vector Norms** | L1 (sum of abs), L2 (Euclidean). Used in regularization and distance. |
| **Matrix Multiplication** | Rows × columns. Core operation in neural networks and linear regression. |
| **Matrix Transpose** | Rows become columns. Needed for backprop and solving linear systems. |
| **Systems of Linear Equations** | Ax = b. Solved via inverse or decomposition. Basis for normal equation in regression. |
| **Eigenvalues & Eigenvectors** | Directions that stay unchanged under linear transform. Used in PCA, stability analysis. |
| **SVD (Singular Value Decomposition)** | A = UΣVᵀ. Used in PCA, matrix completion, dimensionality reduction. |
| **Eigendecomposition** | A = VΛV⁻¹ for diagonalizable matrices. Used in spectral methods. |

## 2. Calculus

| Topic | Explanation |
|-------|-------------|
| **Derivatives** | Rate of change. f'(x) = lim[h→0] (f(x+h)-f(x))/h. Slope of tangent. |
| **Chain Rule** | d/dx[f(g(x))] = f'(g(x))·g'(x). Foundation of backpropagation in neural nets. |
| **Partial Derivatives** | Derivative with respect to one variable, others held constant. ∂f/∂x. |
| **Gradients** | Vector of all partial derivatives. ∇f points toward steepest ascent. |
| **Gradient Descent** | x_new = x - α∇f(x). Move opposite to gradient to minimize. |
| **Stochastic Gradient Descent** | Use one/mini-batch sample per update. Faster, noisier. |
| **Jacobian** | Matrix of first partial derivatives. Used in multi-output backprop. |
| **Hessian** | Matrix of second derivatives. Curvature; used in second-order optimization. |

## 3. Optimization

| Topic | Explanation |
|-------|-------------|
| **Convex vs Non-Convex** | Convex: one global minimum. Non-convex (like neural nets): many local minima. |
| **Learning Rate (α)** | Step size in gradient descent. Too large = divergence; too small = slow convergence. |
| **Lagrange Multipliers** | Method for constrained optimization. Used in SVM derivation. |

## 4. Descriptive Statistics

| Topic | Explanation |
|-------|-------------|
| **Mean, Median, Mode** | Mean = average; median = middle; mode = most frequent. Median robust to outliers. |
| **Variance & Std Dev** | Variance = E[(X-μ)²]; Std = √Variance. Measure spread. |
| **IQR** | Q3 - Q1. Robust spread measure; used in box plots and outlier detection. |
| **Normal Distribution** | Bell curve. Central limit theorem: sums tend to normal. |
| **Z-score** | (x - μ)/σ. Number of std devs from mean. |z| > 3 often outlier. |

## 5. Probability Theory

| Topic | Explanation |
|-------|-------------|
| **Conditional Probability** | P(A|B) = P(A∩B)/P(B). Core of Naive Bayes, P(y\|x). |
| **Bayes' Theorem** | P(A|B) = P(B|A)P(A)/P(B). Updates beliefs with evidence. |
| **Expectation** | E[X] = Σ x·P(X=x). Average outcome. Used in loss functions. |
| **Law of Large Numbers** | Sample mean → population mean as n → ∞. |
| **Central Limit Theorem** | Sample means follow normal distribution for large n. |

## 6. Hypothesis Testing

| Topic | Explanation |
|-------|-------------|
| **Null (H0) vs Alternative (H1)** | H0: no effect; H1: effect exists. Test rejects or fails to reject H0. |
| **p-value** | P(observed data \| H0 true). Small p-value → reject H0. |
| **Type I Error** | False positive: reject true H0. Controlled by α (e.g., 0.05). |
| **Type II Error** | False negative: fail to reject false H0. |
| **t-test** | Compare means. One-sample, two-sample, paired. |
| **Chi-Square** | Test independence of categorical variables. |

## 7. Information Theory

| Topic | Explanation |
|-------|-------------|
| **Entropy** | H(X) = -Σ P(x)log P(x). Measure of uncertainty. Used in decision trees. |
| **Cross-Entropy** | -Σ y log(ŷ). Standard classification loss. |
| **KL Divergence** | Measures difference between two distributions. Used in VAEs. |

---

# CLASSICAL ML TOPICS

## 1. Fundamentals

| Topic | Explanation |
|-------|-------------|
| **Supervised vs Unsupervised** | Supervised: labeled data (y given). Unsupervised: no labels (clustering, PCA). |
| **Bias-Variance Tradeoff** | High bias = underfitting; high variance = overfitting. Goal: balance. |
| **Overfitting** | Model memorizes training data, fails on new data. Fix: regularization, more data. |
| **K-Fold CV** | Split data into K folds; train on K-1, test on 1; rotate. Robust performance estimate. |
| **Stratified K-Fold** | K-Fold preserving class proportions. Important for imbalanced data. |

## 2. Data Preprocessing

| Topic | Explanation |
|-------|-------------|
| **Standardization** | (x - μ)/σ. Zero mean, unit variance. Required for SVM, neural nets. |
| **Min-Max Scaling** | (x - min)/(max - min). Scales to [0,1]. |
| **One-Hot Encoding** | Categorical → binary columns. For nominal categories. |
| **Imputation** | Fill missing: mean, median, mode, or learned (e.g., KNN). |

## 3. Linear Regression

| Topic | Explanation |
|-------|-------------|
| **Simple Linear Regression** | y = wx + b. One feature. Minimize MSE. |
| **Multiple Regression** | y = w₁x₁ + … + wₙxₙ + b. Many features. |
| **Normal Equation** | Closed-form: w = (XᵀX)⁻¹Xᵀy. No iteration. |
| **Ridge (L2)** | Add λ||w||² to loss. Shrinks coefficients. |
| **Lasso (L1)** | Add λ||w||₁. Can zero out coefficients (feature selection). |
| **Elastic Net** | L1 + L2. Combines both. |

## 4. Classification

| Topic | Explanation |
|-------|-------------|
| **Logistic Regression** | P(y=1|x) = sigmoid(w·x+b). Despite name, classification. |
| **KNN** | Classify by majority vote of k nearest neighbors. Non-parametric. |
| **Naive Bayes** | P(y|x) ∝ P(y)Π P(xᵢ|y). Assumes feature independence. |
| **SVM** | Find max-margin hyperplane. Kernel trick for non-linear. |
| **SMOTE** | Synthetic oversampling for imbalanced classes. |
| **Decision Boundary** | Surface separating classes. Linear or non-linear. |

## 5. Tree-Based Models

| Topic | Explanation |
|-------|-------------|
| **Decision Tree** | Split on features; leaf = prediction. Interpretable. |
| **Entropy / Gini** | Splitting criteria. Lower = purer node. |
| **Random Forest** | Ensemble of trees; bootstrap + feature subset. Reduces variance. |
| **Gradient Boosting** | Sequentially add trees to correct previous errors. |
| **XGBoost** | Fast, regularized gradient boosting. Industry standard. |
| **Feature Importance** | How much each feature reduces impurity across splits. |

## 6. Unsupervised Learning

| Topic | Explanation |
|-------|-------------|
| **K-Means** | Partition into k clusters by minimizing within-cluster variance. |
| **Elbow Method** | Plot inertia vs k; choose "elbow" for optimal k. |
| **Hierarchical Clustering** | Build dendrogram; merge/split by linkage. |
| **DBSCAN** | Density-based. Finds arbitrary shapes; handles noise. |
| **PCA** | Linear projection to maximize variance. Uses SVD. |
| **t-SNE** | Non-linear projection for visualization. Preserves local structure. |
| **Isolation Forest** | Anomaly detection: isolates outliers with fewer splits. |

## 7. Metrics

| Topic | Explanation |
|-------|-------------|
| **Accuracy** | (TP+TN)/total. Misleading for imbalanced data. |
| **Precision** | TP/(TP+FP). Of predicted positive, how many correct? |
| **Recall** | TP/(TP+FN). Of actual positive, how many found? |
| **F1-Score** | 2·P·R/(P+R). Harmonic mean. |
| **ROC-AUC** | Area under ROC curve. Threshold-independent; 1=perfect. |
| **MSE / MAE / R²** | Regression: MSE=squared error; MAE=absolute; R²=variance explained. |

## 8. Hyperparameter Tuning

| Topic | Explanation |
|-------|-------------|
| **Grid Search** | Exhaustive over hyperparameter grid. Simple but slow. |
| **Random Search** | Sample randomly. Often better than grid. |
| **Bayesian Optimization** | Model performance; suggest next hyperparameters. Efficient. |

---

# DEEP LEARNING TOPICS

## 1. Neural Networks Basics

| Topic | Explanation |
|-------|-------------|
| **Perceptron** | Single neuron: y = activation(w·x + b). Linear classifier. |
| **Activation Functions** | Sigmoid (0,1), Tanh (-1,1), ReLU (max(0,x)). Introduce non-linearity. |
| **Forward Pass** | Compute output layer by layer from input. |
| **Backpropagation** | Chain rule to compute gradients w.r.t. all weights. |
| **Vanishing Gradient** | Gradients → 0 in deep nets. ReLU, skip connections help. |
| **Gradient Clipping** | Cap gradient norm. Prevents exploding gradients in RNNs. |

## 2. Training

| Topic | Explanation |
|-------|-------------|
| **Cross-Entropy Loss** | Standard for classification. -Σ y log ŷ. |
| **Adam** | Adaptive learning rate. Combines momentum + RMSprop. Default choice. |
| **Batch Normalization** | Normalize layer inputs. Faster training, acts as regularizer. |
| **Dropout** | Randomly zero neurons during training. Reduces overfitting. |
| **Learning Rate Schedule** | Decay LR over time. Step, exponential, cosine. |
| **Weight Initialization** | Xavier/He: scale by fan-in/fan-out. Prevents saturation. |

## 3. CNNs

| Topic | Explanation |
|-------|-------------|
| **Convolution** | Sliding filter over input. Detects local patterns (edges, textures). |
| **Pooling** | Downsample (max/avg). Reduces size; adds invariance. |
| **LeNet, VGG, ResNet** | Classic architectures. ResNet: skip connections solve vanishing gradient. |
| **Transfer Learning** | Use pretrained model; fine-tune on your data. Saves compute. |
| **Object Detection** | YOLO, R-CNN: localize + classify objects in images. |

## 4. RNNs & NLP

| Topic | Explanation |
|-------|-------------|
| **RNN** | Recurrent: hidden state carries sequence info. |
| **LSTM** | Gates (forget, input, output) control flow. Addresses vanishing gradient. |
| **Word Embeddings** | Dense vectors (Word2Vec, GloVe). Capture semantic similarity. |
| **Attention** | Weighted sum over inputs. "Focus" on relevant parts. |
| **Transformer** | Self-attention only; no recurrence. Basis of BERT, GPT. |
| **BERT / GPT** | BERT: encoder, bidirectional. GPT: decoder, autoregressive. |

## 5. Generative Models

| Topic | Explanation |
|-------|-------------|
| **GAN** | Generator creates fake; discriminator tries to tell apart. Adversarial training. |
| **Autoencoder** | Encode to latent; decode to reconstruct. Unsupervised representation. |
| **VAE** | Probabilistic autoencoder. Learns latent distribution. |
| **Diffusion** | Iteratively denoise. State-of-the-art image generation. |

## 6. Reinforcement Learning

| Topic | Explanation |
|-------|-------------|
| **Agent, Environment** | Agent takes actions; environment returns state + reward. |
| **Q-Learning** | Learn Q(s,a) = expected return. Off-policy, tabular. |
| **DQN** | Q-Learning with neural network. Experience replay, target network. |
| **Policy Gradient** | Directly optimize policy. On-policy. |

---

# BOOK 1: Grokking Deep Learning (by Andrew W. Trask)

**Location:** `e:\Ai Ml\Book\Grokking Deep Learning by Andrew W. Trask (z-lib.org).pdf`  
**Focus:** Build neural networks from scratch with NumPy. Low barrier to entry.

## Main Chapters & Topics

| Chapter | Title | Key Topics |
|---------|-------|------------|
| 1 | Introducing Deep Learning | Why learn DL, low barrier, what you need (Python, NumPy) |
| 2 | Fundamental Concepts | What is ML, what is DL, how machines learn |
| 3 | Introduction to Neural Prediction | Forward propagation, single neuron |
| 4 | Introduction to Neural Learning | Gradient descent, weight updates |
| 5 | Learning Multiple Weights | Generalizing gradient descent, multiple inputs |
| 6 | Building First Deep Network | Backpropagation, multi-layer |
| 7 | Picturing Neural Networks | Visualization, mental models |
| 8 | Regularization and Batching | Learning signal vs noise, batching |
| 9 | Modeling Probabilities and Nonlinearities | Sigmoid, probability outputs |
| 10 | Convolutional Neural Networks | Edges and corners, weight sharing |
| 11 | Natural Language Processing | Word embeddings, semantic similarity |
| 12 | Recurrent Layers | Variable-length data, Shakespeare-style generation |
| 13 | Deep Learning Framework | Automatic differentiation, building a framework |

---

# BOOK 2: Deep Learning (by Goodfellow, Bengio, Courville)

**Reference:** Available free at [deeplearningbook.org](https://www.deeplearningbook.org/)  
**Focus:** Comprehensive mathematical and conceptual foundation. Academic standard.

## Part I: Applied Math and ML Basics

| Chapter | Title | Key Topics |
|---------|-------|------------|
| 2 | Linear Algebra | Scalars, vectors, matrices, eigenvalues, SVD |
| 3 | Probability and Information Theory | Random variables, Bayes, entropy, KL divergence |
| 4 | Numerical Computation | Overflow, conditioning, gradient-based optimization |
| 5 | Machine Learning Basics | Capacity, overfitting, regularization, validation |

## Part II: Modern Practical Deep Networks

| Chapter | Title | Key Topics |
|---------|-------|------------|
| 6 | Deep Feedforward Networks | MLP, activation, universal approximation |
| 7 | Regularization for Deep Learning | Parameter norm penalty, dropout, data augmentation |
| 8 | Optimization for Training | SGD, momentum, adaptive learning rates, second-order |
| 9 | Convolutional Networks | Convolution, pooling, CNN architectures |
| 10 | Sequence Modeling | RNN, LSTM, encoder-decoder |
| 11 | Practical Methodology | Debugging, hyperparameters, supervision |
| 12 | Applications | Computer vision, speech, NLP |

## Part III: Deep Learning Research

| Chapter | Title | Key Topics |
|---------|-------|------------|
| 13 | Linear Factor Models | PCA, ICA, sparse coding |
| 14 | Autoencoders | Undercomplete, denoising, contractive |
| 15 | Representation Learning | Greedy layer-wise, transfer learning |
| 16–20 | Generative Models, Inference | Structured models, Monte Carlo, generative models |

---

## Additional Book: Hands-On Machine Learning (Géron)

**Common reference for classical ML + practical DL.** Covers: ML landscape, end-to-end projects, classical algorithms (linear, SVM, trees, ensembles), unsupervised learning, neural nets, CNNs, RNNs, deployment, and reinforcement learning.

---

## How to Use This File

1. **Interview prep:** Scan topics; ensure you can explain each in 1–2 sentences.
2. **Academic study:** Map topics to your syllabus; use as checklist.
3. **Book mapping:** Use the book sections to find where each topic is covered.
4. **Cross-reference:** See `LEARNING_PATH.md` for the week-by-week curriculum; this file expands individual topics for revision.

---

*Last updated: Feb 2025*
