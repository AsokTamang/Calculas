# 📈 Linear Regression for Sales Prediction

## 📌 Overview
This project implements a **simple linear regression model** to predict **sales** based on **TV marketing expenses**. The objective is to understand linear regression both **theoretically** and **practically** by applying multiple approaches to the same problem.

The assignment explores three different methods:
- Linear regression using **NumPy**
- Linear regression using **Scikit-Learn**
- Linear regression built **from scratch** using **gradient descent**

---

## 🎯 Objective
- Analyze the relationship between TV advertising budget and sales  
- Implement linear regression using different techniques  
- Understand the **sum of squares cost function**  
- Learn how **gradient descent** optimizes model parameters  

---

## 🧠 Methods Used

### 1️⃣ Linear Regression with NumPy
- Uses NumPy operations to compute predictions  
- Implements the **Mean Squared Error (MSE)** loss function  
- Calculates gradients analytically  
- Updates parameters using gradient descent  

This approach helps build intuition about the mathematics behind linear regression.

---

### 2️⃣ Linear Regression with Scikit-Learn
- Uses `LinearRegression` from `sklearn.linear_model`  
- Trains the model using the `.fit()` method  
- Makes predictions using the `.predict()` method  
- Extracts learned parameters:
  - `coef_` (slope)
  - `intercept_` (bias)

This approach demonstrates how linear regression is applied in real-world machine learning workflows.

---

### 3️⃣ Linear Regression from Scratch (Gradient Descent)
- Defines the **sum of squared errors** cost function:

\[
E = \frac{1}{2n} \sum (mx + b - y)^2
\]

- Computes partial derivatives with respect to:
  - slope (`m`)
  - intercept (`b`)
- Iteratively updates parameters using gradient descent  
- Shows how optimization works without external ML libraries  

---

## 🧮 Cost Function
The cost function used in this project is the **Mean Squared Error (MSE)**:

\[
E = \frac{1}{2n} \sum (y_{pred} - y)^2
\]

This measures how far predictions are from actual sales values and is minimized during training.

---

## 🛠️ Technologies Used
- Python  
- NumPy  
- Scikit-Learn  
- Matplotlib  

---

## 📊 Results
- All three approaches produce similar regression lines  
- Scikit-Learn provides the fastest and most concise implementation  
- Gradient descent offers the best insight into how learning occurs internally  

---

## 📚 Key Learnings
- How linear regression models are trained  
- Why normalization improves gradient descent  
- How loss functions guide model optimization  
- The connection between mathematical formulas and vectorized NumPy code  

---

## 🚀 Conclusion
This assignment shows that while libraries like Scikit-Learn simplify model development, understanding the underlying mathematics—especially **gradient descent** and **cost functions**—is essential for mastering machine learning.
