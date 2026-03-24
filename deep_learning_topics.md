# Deep Learning Topics (Academic & Job Preparation)

> **Full explanations:** See `MAIN_EXPLANATION.md` for each topic's definition and use.

## 1. Neural Networks Basics
- Perceptron
- Single Neuron (Weights, Bias, Activation)
- Activation Functions: Sigmoid
- Activation Functions: Tanh
- Activation Functions: ReLU
- Activation Functions: Leaky ReLU
- Activation Functions: ELU
- Activation Functions: Softmax
- Forward Pass
- MLP (Multi-Layer Perceptron)
- Building MLP from Scratch
- Backpropagation
- Chain Rule in Backprop
- Gradient Flow
- Gradient Checking
- Vanishing Gradient Problem
- Exploding Gradient Problem
- Gradient Clipping

## 2. Training Deep Networks
- Loss Functions: MSE
- Loss Functions: Cross-Entropy
- Loss Functions: Binary Cross-Entropy
- Loss Functions: Categorical Cross-Entropy
- Loss Functions: Hinge Loss
- Optimizers: SGD
- Optimizers: SGD with Momentum
- Optimizers: Nesterov Momentum
- Optimizers: AdaGrad
- Optimizers: RMSprop
- Optimizers: Adam
- Optimizers: AdamW
- Learning Rate
- Learning Rate Schedules: Step Decay
- Learning Rate Schedules: Exponential Decay
- Learning Rate Schedules: Cosine Annealing
- Learning Rate Schedules: Warmup
- Batch Size: Full Batch, Mini-Batch, Stochastic
- Epochs
- Batch Normalization
- Layer Normalization
- Dropout
- Early Stopping
- Weight Initialization (Xavier, He)
- Regularization: L1, L2
- Data Augmentation

## 3. Frameworks
- TensorFlow/Keras Introduction
- PyTorch Introduction
- Sequential vs Functional API
- Model Building
- Training Loop
- Callbacks
- Model Saving/Loading

## 4. Convolutional Neural Networks (CNNs)
- Convolution Operation
- Filters (Kernels)
- Stride
- Padding (Valid, Same)
- Feature Maps
- Pooling: Max Pooling
- Pooling: Average Pooling
- Pooling: Global Average Pooling
- Receptive Field
- CNN Architectures: LeNet
- CNN Architectures: AlexNet
- CNN Architectures: VGG
- CNN Architectures: ResNet (Residual Connections)
- CNN Architectures: Inception
- CNN Architectures: MobileNet
- CNN Architectures: EfficientNet
- Transfer Learning
- Fine-Tuning
- Image Augmentation: Rotation, Flip, Crop
- Image Augmentation: Color Jittering
- Image Augmentation: Cutout, Mixup
- Object Detection: R-CNN, Fast R-CNN
- Object Detection: YOLO
- Object Detection: SSD
- Semantic Segmentation
- Instance Segmentation

## 5. Recurrent Neural Networks (RNNs)
- Sequential Data
- RNN Architecture
- RNN: Vanishing Gradients
- LSTM (Long Short-Term Memory)
- LSTM: Forget, Input, Output Gates
- GRU (Gated Recurrent Unit)
- Bidirectional RNN
- Many-to-One, One-to-Many, Many-to-Many
- Sequence-to-Sequence (Seq2Seq)
- Encoder-Decoder Architecture

## 6. Natural Language Processing (NLP)
- Text Preprocessing
- Tokenization (Word, Subword, Character)
- Tokenization: WordPiece, BPE
- Vectorization: Count Vectorization
- Vectorization: TF-IDF
- Word Embeddings: Word2Vec (CBOW, Skip-gram)
- Word Embeddings: GloVe
- Word Embeddings: FastText
- Padding and Truncation
- Named Entity Recognition (NER)
- Part-of-Speech Tagging
- Sentiment Analysis
- Text Classification

## 7. Attention & Transformers
- Attention Mechanism
- Self-Attention
- Query, Key, Value (Q, K, V)
- Scaled Dot-Product Attention
- Multi-Head Attention
- Positional Encoding
- Transformer Architecture
- Encoder-Only: BERT
- Decoder-Only: GPT
- Encoder-Decoder: T5
- Fine-Tuning Pretrained Models
- Hugging Face Transformers
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)

## 8. Generative Models
- Generative Adversarial Networks (GANs)
- GAN: Generator
- GAN: Discriminator
- GAN: Adversarial Training
- GAN: DCGAN
- GAN: Conditional GAN
- GAN: Training Instability
- Autoencoders
- Autoencoder: Encoder-Decoder
- Denoising Autoencoder
- Variational Autoencoders (VAE)
- VAE: Reparameterization Trick
- VAE: KL Divergence
- Diffusion Models (Intro)

## 9. Reinforcement Learning (Intro)
- Agent, Environment, State, Action, Reward
- Policy
- Value Function
- Q-Learning
- Deep Q-Networks (DQN)
- Policy Gradient
- Actor-Critic

## 10. Model Optimization & Deployment
- Model Compression
- Quantization (Float32 → Int8)
- Pruning
- Knowledge Distillation
- TensorFlow Lite
- ONNX
- Model Quantization for Edge
- Inference Optimization

## 11. Advanced Topics
- Neural Architecture Search (NAS)
- AutoML
- Federated Learning (Intro)
- Contrastive Learning (Intro)
- Self-Supervised Learning (Intro)
- Few-Shot Learning (Intro)
- Explainability: Grad-CAM
- Explainability: SHAP, LIME
