# 3-Month Machine Learning & Deep Learning Learning Path

## Welcome! 🚀

This is your comprehensive, hands-on learning path to master Machine Learning and Deep Learning from fundamentals to advanced concepts. Designed for intermediate learners with 10-20 hours/week commitment.

## 📋 Quick Start

### Prerequisites
- Python 3.9+ installed
- Basic programming knowledge
- High school mathematics
- 10-20 hours/week commitment

### Setup

```bash
# Create virtual environment
python -m venv ml_env
source ml_env/bin/activate  # On Windows: ml_env\Scripts\activate

# Install required packages
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
pip install tensorflow torch torchvision  # For deep learning (Month 3)

# Launch Jupyter
jupyter lab
```

### Installation Guide

Create a `requirements.txt`:
```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=1.0.0
jupyter>=1.0.0
jupyterlab>=3.0.0

# For Deep Learning (Month 3)
tensorflow>=2.8.0
torch>=1.10.0
torchvision>=0.11.0
```

Install: `pip install -r requirements.txt`

## 📚 Curriculum Overview

### Month 1: Foundations (Weeks 1-4)
Build the mathematical and programming foundation for ML.

**Week 1: Python & Math Basics**
- ✅ Python refresher (OOP, functional programming)
- ✅ Linear algebra (vectors, matrices, eigenvalues)
- ✅ Calculus (derivatives, gradients, chain rule)
- 📁 Files: 3 notebooks, exercises, mini project

**Week 2: NumPy, Pandas & Matplotlib**
- NumPy for numerical computing
- Pandas for data manipulation
- Data visualization with Matplotlib/Seaborn
- 📁 Files: 3 notebooks, exercises, EDA project

**Week 3: Statistics & Probability**
- Descriptive statistics
- Probability theory and distributions
- Hypothesis testing
- 📁 Files: 3 notebooks, exercises, A/B test project

**Week 4: Linear Regression**
- Simple and multiple regression
- Gradient descent optimization
- Regularization (Ridge, Lasso, ElasticNet)
- 📁 Files: 4 notebooks, exercises, house price prediction

### Month 2: Classical Machine Learning (Weeks 5-8)
Master traditional ML algorithms and techniques.

**Week 5: Classification Algorithms**
- Logistic regression
- K-Nearest Neighbors (KNN)
- Naive Bayes
- Support Vector Machines (SVM)
- 📁 Files: 4 notebooks, exercises, spam detector

**Week 6: Tree-Based Models**
- Decision trees
- Random forests
- Gradient boosting (XGBoost, LightGBM)
- Feature importance
- 📁 Files: 4 notebooks, exercises, fraud detection

**Week 7: Unsupervised Learning**
- K-means clustering
- Hierarchical clustering
- PCA (dimensionality reduction)
- Anomaly detection
- 📁 Files: 4 notebooks, exercises, customer segmentation

**Week 8: Model Evaluation & Deployment**
- Cross-validation techniques
- Evaluation metrics
- Hyperparameter tuning
- Model deployment basics
- 📁 Files: 4 notebooks, exercises, ML pipeline project

### Month 3: Deep Learning (Weeks 9-12)
Dive into neural networks and modern deep learning.

**Week 9: Neural Networks Basics**
- Perceptron and MLP
- Backpropagation
- TensorFlow/Keras introduction
- PyTorch basics
- 📁 Files: 5 notebooks, exercises, MNIST project

**Week 10: CNNs & Computer Vision**
- Convolutional operations
- CNN architectures (ResNet, EfficientNet)
- Transfer learning
- Object detection basics
- 📁 Files: 5 notebooks, exercises, image classifier

**Week 11: RNNs & NLP**
- Text preprocessing
- RNN, LSTM, GRU
- Attention mechanisms
- Transformers (BERT, GPT basics)
- 📁 Files: 5 notebooks, exercises, sentiment analysis

**Week 12: Advanced DL & Capstone**
- GANs (Generative Adversarial Networks)
- Autoencoders
- Reinforcement learning intro
- Full capstone project
- 📁 Files: 4 notebooks, capstone project options

## 🗂️ Repository Structure

```
ML-DL-Learning/
├── README.md (this file)
├── requirements.txt
├── generate_content.py
│
├── Month-1-Foundations/
│   ├── Week-1-Python-Math-Basics/
│   │   ├── 01_python_refresher.ipynb ✅
│   │   ├── 02_linear_algebra.ipynb ✅
│   │   ├── 03_calculus_basics.ipynb ✅
│   │   ├── exercises.md ✅
│   │   ├── mini_project.md ✅
│   │   └── resources.md ✅
│   ├── Week-2-NumPy-Pandas-Matplotlib/
│   ├── Week-3-Statistics-Probability/
│   └── Week-4-Linear-Regression/
│
├── Month-2-Classical-ML/
│   ├── Week-5-Classification-Algorithms/
│   ├── Week-6-Tree-Based-Models/
│   ├── Week-7-Unsupervised-Learning/
│   └── Week-8-Model-Evaluation-Deployment/
│
├── Month-3-Deep-Learning/
│   ├── Week-9-Neural-Networks-Basics/
│   ├── Week-10-CNNs-Computer-Vision/
│   ├── Week-11-RNNs-NLP/
│   └── Week-12-Advanced-DL-Capstone/
│
└── Resources/
    ├── datasets/
    ├── cheatsheets/
    └── reference-books/
```

## 📅 Weekly Study Schedule

Recommended time allocation (10-20 hours/week):

- **Monday-Tuesday (4-6 hours):** Theory & Concepts
  - Read notebooks
  - Watch recommended videos
  - Take notes

- **Wednesday-Thursday (4-6 hours):** Hands-on Coding
  - Work through notebook examples
  - Experiment with code
  - Debug and understand errors

- **Friday (2-3 hours):** Practice Exercises
  - Complete exercise problems
  - Review solutions
  - Identify weak areas

- **Weekend (3-5 hours):** Mini Project
  - Apply week's knowledge
  - Build something real
  - Document your work

- **Sunday Evening (1-2 hours):** Review & Plan
  - Summarize key learnings
  - Prepare for next week
  - Update progress tracker

## 🎯 Learning Approach

### Active Learning
- **Don't just read** - Type out all code examples
- **Experiment** - Modify parameters, try variations
- **Break things** - Learn from errors
- **Implement from scratch** - Understand internals before using libraries

### Progressive Difficulty
- Each week builds on previous knowledge
- Start with theory, move to practice
- Simple examples → Complex applications
- Guided projects → Independent work

### Hands-On Focus
- Every concept has code examples
- Multiple exercises per topic
- Weekly mini projects
- Monthly capstone projects

## 📊 Progress Tracking

Create a `progress.md` file to track your journey:

```markdown
# My ML/DL Learning Progress

## Month 1: Foundations
- [x] Week 1: Python & Math Basics (Completed: 2024-XX-XX)
- [ ] Week 2: NumPy, Pandas & Matplotlib
- [ ] Week 3: Statistics & Probability
- [ ] Week 4: Linear Regression

## Month 2: Classical ML
- [ ] Week 5: Classification
- [ ] Week 6: Tree-Based Models
- [ ] Week 7: Unsupervised Learning
- [ ] Week 8: Evaluation & Deployment

## Month 3: Deep Learning
- [ ] Week 9: Neural Networks
- [ ] Week 10: CNNs & Computer Vision
- [ ] Week 11: RNNs & NLP
- [ ] Week 12: Advanced DL & Capstone

## Projects Completed
1. Matrix Calculator (Week 1)
2. ...

## Key Learnings
- ...
```

## 🛠️ Tools & Technologies

### Core Libraries
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation
- **Matplotlib/Seaborn**: Visualization
- **Scikit-learn**: Classical ML algorithms

### Deep Learning Frameworks
- **TensorFlow/Keras**: Industry standard
- **PyTorch**: Research and flexibility

### Development Tools
- **Jupyter Lab**: Interactive development
- **Git**: Version control
- **VS Code/PyCharm**: Code editors

## 📖 Additional Resources

### Online Courses
- **Andrew Ng's ML Course** (Coursera)
- **Fast.ai** (Practical Deep Learning)
- **DeepLearning.AI Specialization**

### Books
- "Hands-On Machine Learning" by Aurélien Géron
- "Deep Learning" by Goodfellow, Bengio, Courville
- "Pattern Recognition and Machine Learning" by Bishop

### YouTube Channels
- 3Blue1Brown (Math visualization)
- StatQuest (Statistics)
- Sentdex (Python & ML)
- Two Minute Papers (Latest research)

### Websites
- Kaggle (Competitions & datasets)
- Papers With Code (Latest research)
- Towards Data Science (Articles)
- Distill.pub (Visual explanations)

## 🤝 Community & Support

### Get Help
- **Stack Overflow**: Programming questions
- **Cross Validated**: Statistics & ML theory
- **Reddit**: r/learnmachinelearning, r/MachineLearning
- **Discord**: Various ML learning servers

### Share Your Progress
- Create a GitHub repository
- Write blog posts
- Share on LinkedIn/Twitter
- Join study groups

## 🎓 Certification & Portfolio

### Build Your Portfolio
1. **GitHub Repository**
   - Upload all projects
   - Write good README files
   - Document your code

2. **Blog/Medium**
   - Explain concepts you learned
   - Share project walkthroughs
   - Teaching reinforces learning

3. **Kaggle**
   - Participate in competitions
   - Share notebooks
   - Build reputation

### Capstone Project Ideas
- End-to-end ML pipeline
- Computer vision application
- NLP chatbot
- Recommendation system
- Time series forecasting
- Anomaly detection system

## 🚀 After 3 Months

### Next Steps
1. **Advanced Topics**
   - Reinforcement Learning
   - Graph Neural Networks
   - Meta-Learning
   - MLOps & Production Systems

2. **Specialization**
   - Computer Vision
   - Natural Language Processing
   - Time Series Analysis
   - Recommender Systems

3. **Real-World Experience**
   - Kaggle competitions
   - Open source contributions
   - Freelance projects
   - Job applications

4. **Continuous Learning**
   - Read research papers
   - Implement papers from scratch
   - Stay updated with latest developments

## 💡 Tips for Success

### Do's
✅ Practice daily (consistency > intensity)  
✅ Implement algorithms from scratch first  
✅ Understand the math behind algorithms  
✅ Work on real datasets  
✅ Document your learning  
✅ Ask questions when stuck  
✅ Review and revise regularly  

### Don'ts
❌ Don't rush through material  
❌ Don't skip the math  
❌ Don't just copy-paste code  
❌ Don't work in isolation  
❌ Don't aim for perfection  
❌ Don't give up when stuck  

## 🐛 Troubleshooting

### Common Issues

**Installation Problems**
```bash
# Use virtual environment
python -m venv ml_env
source ml_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install packages one by one if batch fails
pip install numpy
pip install pandas
# etc.
```

**Jupyter Not Starting**
```bash
# Reinstall jupyter
pip uninstall jupyter jupyterlab
pip install jupyter jupyterlab

# Or use
python -m jupyter lab
```

**Import Errors**
- Ensure virtual environment is activated
- Check package is installed: `pip list`
- Reinstall package: `pip install --upgrade package_name`

## 📞 Contact & Feedback

This is a self-paced learning path. Adapt it to your needs:
- Skip topics you already know
- Spend more time on challenging areas
- Add additional resources that work for you
- Adjust the pace based on your schedule

## 📝 License

This learning path is for educational purposes. Feel free to:
- Use for personal learning
- Share with others
- Modify to fit your needs
- Contribute improvements

## 🙏 Acknowledgments

This curriculum is inspired by:
- Andrew Ng's Machine Learning course
- Fast.ai's practical approach
- Stanford CS229 and CS231n
- MIT 6.S191
- Various online resources and textbooks

---

## Ready to Start?

1. ✅ Set up your environment
2. ✅ Create a progress tracker
3. ✅ Join a learning community
4. ✅ Start with Week 1!

**Remember:** The journey of a thousand miles begins with a single step. You've got this! 💪

---

*Last Updated: 2024*  
*Version: 1.0*  
*Status: Active Development*

Happy Learning! 🎉
