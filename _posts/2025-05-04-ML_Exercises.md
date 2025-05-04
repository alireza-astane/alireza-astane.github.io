---
title: ML_Exercises
date: 2025-05-04 15:09:21 +0000
categories: [GitHub, Repositories]
tags: [github, ml_exercises]
---

---
description: No description available.
---
---
toc: false
---

# Machine Learning Project

This repository contains a collection of machine learning notebooks and resources, organized into different categories. Below is an overview of the project structure and the contents of each folder.

## Project Structure

```
01-supervised/
    decision_trees.ipynb
    gradient_boosting.ipynb
    linear_regression.ipynb
    logistic_regression.ipynb
    svm_digits.ipynb
    usa_housing_model.pkl
02-unsupervised/
    hierarchical_dbscan.ipynb
    kmeans_clustering.gif
    kmeans_iris.ipynb
    tsne_visualization.ipynb
03-preprocessing-eda/
    eda_titanic.ipynb
    feature_selection.ipynb
    preprocessing_pipeline.ipynb
04-evaluation-tuning/
    crossval_gridsearch.ipynb
    model_metrics.ipynb
05-advanced/
    ensemble_comparison.ipynb
    nlp_sentiment_analysis.ipynb
    time_series_forecasting.ipynb
LICENSE
README.md
```

---

## Folder Details

### 01-supervised/
This folder contains notebooks related to supervised learning techniques:
- **`decision_trees.ipynb`**: Implementation of decision trees with feature importance visualization.
- **`gradient_boosting.ipynb`**: Comparison of XGBoost and LightGBM with ROC curve analysis.
- **`linear_regression.ipynb`**: Linear regression for predicting housing prices.
- **`logistic_regression.ipynb`**: Logistic regression with metrics like accuracy, confusion matrix, and ROC-AUC.
- **`svm_digits.ipynb`**: Support Vector Machines for digit classification using the MNIST dataset.

### 02-unsupervised/
This folder focuses on unsupervised learning techniques:
- **`hierarchical_dbscan.ipynb`**: HDBSCAN and DBSCAN clustering with visualization of linkage and condensed trees.
- **`kmeans_clustering.gif`**: Animated visualization of K-Means clustering.
- **`kmeans_iris.ipynb`**: K-Means clustering applied to the Iris dataset.
- **`tsne_visualization.ipynb`**: t-SNE for dimensionality reduction and visualization.

### 03-preprocessing-eda/
This folder includes preprocessing and exploratory data analysis (EDA) notebooks:
- **`eda_titanic.ipynb`**: EDA on the Titanic dataset with visualizations, feature engineering, and correlation heatmaps.
- **`feature_selection.ipynb`**: Feature selection using ANOVA F-test, mutual information, and Random Forest importance.
- **`preprocessing_pipeline.ipynb`**: End-to-end preprocessing pipeline with feature scaling, encoding, and model evaluation.

### 04-evaluation-tuning/
This folder contains notebooks for model evaluation and hyperparameter tuning:
- **`crossval_gridsearch.ipynb`**: Cross-validation and grid search for hyperparameter optimization.
- **`model_metrics.ipynb`**: Evaluation metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.

### 05-advanced/
This folder explores advanced machine learning topics:
- **`ensemble_comparison.ipynb`**: Comparison of ensemble methods like Random Forest, Gradient Boosting, and Extra Trees.
- **`nlp_sentiment_analysis.ipynb`**: Sentiment analysis using Naive Bayes on the NLTK movie reviews dataset.
- **`time_series_forecasting.ipynb`**: Time series forecasting with models like ARIMA and Holt-Winters.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

--- 

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/alireza-astane/ML_Exercises.git
   cd ml-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Explore the notebooks in the `notebooks/` directory.

--- 

