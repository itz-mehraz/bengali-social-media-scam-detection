# Social Media Scam Detection Using Machine Learning

A machine learning-based thesis project for detecting scam-related job and social media posts using English and Bengali text data.

---

## Project Overview

Online scams are increasing rapidly across job portals and social media platforms. This project proposes a machine learning-based approach to detect scam-related posts by analyzing textual patterns from both a public job-posting dataset and a Facebook-style dataset. The study focuses on cross-domain performance, domain adaptation, and comparative model evaluation.

---

## Research Objectives

- Detect scam and non-scam posts using machine learning
- Analyze the performance of text-based classification models
- Evaluate whether a model trained on one dataset can generalize to another
- Improve performance by combining English and Bengali/mixed-language data
- Compare multiple machine learning algorithms to identify the best-performing model

---

## Datasets Used

### 1. Main Dataset
- **Name:** Fake Job Postings Dataset
- **Size:** 17,880 rows
- **Target Column:** `fraudulent`
- **Purpose:** Used as the primary training dataset for baseline modeling

### 2. Facebook Dataset
- **Name:** Facebook Job Post Scam Dataset
- **Size:** 440 rows
- **Target Column:** `label`
- **Purpose:** Used to test domain adaptation and final scam detection performance on social-media-style posts

---

## Methodology

The project was completed in the following stages:

1. Data loading and exploration  
2. Missing value analysis  
3. Text preparation and feature engineering  
4. TF-IDF vectorization  
5. Baseline Logistic Regression training  
6. Cross-dataset testing on Facebook posts  
7. Combined dataset training for adaptation  
8. Strict unseen Facebook-only testing  
9. Final comparison of Logistic Regression, SVM, and Random Forest  

---

## Models Used

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest

---

## Key Findings

- The baseline Logistic Regression model achieved high accuracy on the main dataset
- However, the baseline model failed on Facebook-style posts and predicted all posts as non-scam
- This showed that a model trained only on formal job-post data could not generalize to short social media scam posts
- After combining both datasets, performance improved significantly
- In the final unseen Facebook test, both SVM and Random Forest achieved the best performance

---

## Final Results Summary

| Experiment | Accuracy |
|---|---:|
| Baseline Logistic Regression on Main Dataset | 0.9728 |
| Baseline Model on Facebook Dataset | 0.5000 |
| Improved Logistic Regression on Combined Dataset | 0.9735 |
| Final Logistic Regression on Unseen Facebook Test | 0.9659 |
| Final SVM on Unseen Facebook Test | 1.0000 |
| Final Random Forest on Unseen Facebook Test | 1.0000 |

---

## Why This Study Matters

This project demonstrates that:
- dataset domain matters strongly in scam detection
- models trained on formal job-post data may fail on real social media scam posts
- including Bengali or mixed-language social media data can significantly improve detection performance

This makes the research more practical for real-world scam detection systems.

---

## Repository Structure

```text id="jwl4r1"
bengali-social-media-scam-detection/
│
├── data/
├── models/
├── notebooks/
├── results/
├── src/
├── README.md
└── requirements.txt

Files Included
notebooks/
Social_Media_Scam_Detection.ipynb
models/
best_svm_model.pkl
final_tfidf_vectorizer.pkl
results/
final_facebook_test_results.csv
model_comparison_results.csv
experiment_summary_results.csv
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Google Colab
GitHub
Installation

Install the required packages using:

pip install -r requirements.txt
Author

Mehraz
Software Engineering Student
Machine Learning Thesis Project

Future Work
Use a larger real-world Bengali scam dataset
Apply deep learning models such as LSTM or BERT
Build a real-time scam detection web application
Extend the system for multilingual scam detection
Disclaimer

The reported results are based on the datasets and held-out test split used in this study. Perfect accuracy on the final Facebook test should be interpreted within the scope of this dataset only.


After updating the README, your repo will already look much more thesis-ready. Then the next step is creating a small `src/` script section so your project looks cleaner than just a notebook.
