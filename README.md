# 🤖 5-Day AI & Machine Learning Workshop

Welcome to my **5-Day AI & Machine Learning Workshop** repository.

This repository contains the Python programs, datasets, notes, visualizations, model results, and final project that I worked on during the workshop.

The workshop provided hands-on exposure to **Artificial Intelligence, Machine Learning, Python, NumPy, Pandas, Data Visualization, Supervised Learning, Deep Learning, Generative AI, Prompt Engineering, and Responsible AI**.

---

## 📚 Workshop Overview

| Day          | Topics Covered                                                                                              | Practical Work                            |
| ------------ | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| 🟢 **Day 1** | AI & ML fundamentals, Python basics, Lists, Dictionaries, DataFrames, Slicing                               | Python practice programs                  |
| 🔵 **Day 2** | NumPy, arrays, reshaping, dimensions, statistics                                                            | NumPy & statistical operations            |
| 🟡 **Day 3** | Data cleaning and visualization                                                                             | Data cleaning, charts and graphs          |
| 🟠 **Day 4** | Supervised Learning, Regression, Classification, Decision Trees, Clustering, Neural Networks, Deep Learning | Machine Learning models and visualization |
| 🔴 **Day 5** | Generative AI, LLMs, ChatGPT, Prompt Engineering, Responsible AI                                            | Generative AI concepts and final project  |

---

# 🟢 Day 1 — Introduction to AI, ML & Python

### 🤖 Types of Artificial Intelligence

1. **Narrow AI (Weak AI)**
2. **General AI**
3. **Super AI / Theoretical AI**

### 🧠 Types of Machine Learning

* **Supervised Learning** — Learns from labeled data.
* **Unsupervised Learning** — Finds hidden patterns or groups in unlabeled data.
* **Reinforcement Learning** — Learns through trial and error using rewards and penalties.

### 🐍 Python Fundamentals

During Day 1, I practiced:

* Conditional statements
* Lists
* Dictionaries
* DataFrames
* Index, rows and columns
* Slicing
* Basic list operations

### List Operations

* `insert()`
* `pop()`
* `remove()`
* `extend()`
* `clear()`
* `append()`

### Dictionary

```python
{key: value}
```

---

# 🔵 Day 2 — NumPy & Statistics

Day 2 focused on numerical computing and basic statistical operations.

### 🔢 NumPy Concepts

* `arange()`
* `reshape()`
* `shape`
* `ndim`
* Arithmetic operations

### 📊 Statistical Concepts

* Mean
* Median
* Standard Deviation

---

# 🟡 Day 3 — Data Cleaning & Visualization

Day 3 focused on preparing and understanding data through visualization.

### 🧹 Data Cleaning

Learned the basic process of cleaning and preparing datasets before analysis and machine learning.

### 📈 Data Visualization

Worked with:

* Bar Charts
* Scatter Plots

Scatter plots were used to understand the **spread, distribution, and relationship between data points**.

### 💼 AI/ML Career Paths

We also explored different career opportunities, including:

* AI Engineer
* Data Analyst
* Solution Architect

---

# 🟠 Day 4 — Machine Learning & Deep Learning

Day 4 introduced the practical side of Machine Learning.

## Supervised Learning

### Classification

Classification predicts a category or class.

**Example:** Spam / Not Spam

### Regression

Regression predicts a continuous numerical value.

**Example:** Predicting a student's score.

---

## 📊 Training & Testing Data

A dataset can be divided into training and testing data.

```text
              Dataset
                 │
        ┌────────┴────────┐
        ↓                 ↓
   Training Data      Testing Data
       80%                20%
```

In Python:

```python
test_size = 0.2
```

---

## 🔄 Machine Learning Workflow

```text
Data
  ↓
Data Cleaning
  ↓
Training
  ↓
Testing
  ↓
Prediction
  ↓
Evaluation
```

---

## 🤖 Machine Learning Algorithms

### Linear Regression

Used for predicting a **continuous numerical value** from one or more input features.

### Logistic Regression

Used for classification problems, particularly **binary outcomes**.

### Decision Tree

A tree-like model that makes predictions using a series of decision-making rules.

### K-Means Clustering

An unsupervised learning algorithm that groups data into clusters by assigning data points to nearby centroids.

Scatter plots can be used to visualize clustering results.

---

# 🧠 Neural Networks

Learned the basic structure of a neural network:

```text
Input Layer
     ↓
Hidden Layer(s)
     ↓
Output Layer
```

### Activation Functions

* ReLU
* Sigmoid
* Softmax

---

# 🔥 Deep Learning

Deep learning uses neural networks containing multiple hidden layers.

These models can have millions of parameters and generally require large datasets and significant computational resources such as GPUs for effective training.

### Applications of Deep Learning

* Computer Vision
* Natural Language Processing (NLP)
* Generative AI

---

# 🔴 Day 5 — Generative AI

Day 5 introduced Generative AI and modern AI systems.

## ✨ Generative AI

Generative AI can create new content such as:

* Text
* Images
* Audio
* Other forms of digital content

---

## 🧠 Large Language Models (LLMs)

**LLM = Large Language Model**

An LLM is a neural network trained on a very large amount of text data.

The word **Large** refers to the scale of the model, including its parameters and training data.

---

## 💬 Basic Understanding of How ChatGPT Works

```text
Pre-training
     ↓
Fine-tuning
     ↓
Alignment
     ↓
Inference
     ↓
Response
```

---

# 🪄 Prompt Engineering

Prompt engineering focuses on creating effective instructions to get better results from AI systems.

### Strong Prompt Structure

| Component       | Purpose                                        |
| --------------- | ---------------------------------------------- |
| **Role**        | Who should the AI act as?                      |
| **Task**        | What should the AI do?                         |
| **Context**     | What background information is required?       |
| **Constraints** | What limitations or format should be followed? |
| **Output**      | What should the final result look like?        |

---

# 🛡️ Responsible AI

We also discussed important considerations when working with AI:

* Bias
* Privacy
* Limitations of AI
* Responsible use of AI

---

# 🚀 Final Project

As the final part of the workshop, I developed a practical **AI/ML project** applying concepts learned throughout the five days.

## 📌 Project

**Student Score Prediction / Analysis**

The project works with student score data and demonstrates the use of Python and Machine Learning concepts to analyze data and generate model results.

### 📂 Project Files

```text
Final Project
│
├── project.py
├── student_scores_clean.csv
├── model_results.png
└── notes
```

### 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Machine Learning

### 🔄 Project Workflow

```text
Student Dataset
       ↓
Data Cleaning
       ↓
Data Analysis
       ↓
Data Visualization
       ↓
Model Training
       ↓
Prediction
       ↓
Model Evaluation
       ↓
Results
```

### 📊 Model Results

The generated model results and visualizations are included in:

`model_results.png`

---

# 📁 Repository Structure

```text
AI-ML/
│
├── day1.1.py
├── day1.2.py
├── day1.3.py
├── day1.4.py
│
├── day2.py
│
├── day3.py
│
├── day4.1.py
├── day4.2.py
│
├── day5.py
│
├── project.py
│
├── student_scores_clean.csv
├── mall_customers.csv
│
├── model_results.png
│
├── notes
│
└── README.md
```

---

# 🎓 Key Learning Outcomes

After completing the workshop, I gained practical exposure to:

* Artificial Intelligence fundamentals
* Types of Machine Learning
* Python programming for AI/ML
* NumPy
* Pandas and DataFrames
* Data cleaning
* Data visualization
* Statistics
* Supervised Learning
* Classification
* Regression
* Decision Trees
* K-Means Clustering
* Neural Networks
* Deep Learning
* Generative AI
* Large Language Models
* Prompt Engineering
* Responsible AI
* Building an AI/ML project

---

# 🙏 Acknowledgement

I would like to thank **CSITABMC** for organizing the **5-Day AI & Machine Learning Workshop** and providing me with the opportunity to gain practical knowledge and hands-on experience in Artificial Intelligence and Machine Learning.

---

⭐ **This repository represents my learning journey, practical exercises, and final project completed during the 5-Day AI & Machine Learning Workshop.**
