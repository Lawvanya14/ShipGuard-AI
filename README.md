ShipGuard AI
Intelligent Delivery Delay Risk Prediction System

Project Overview

ShipGuard AI is an end-to-end machine learning pipeline developed to predict high-risk delivery delays in logistics operations.

The system evaluates multiple classification models, compares their performance using business-relevant metrics, and selects the most suitable model for deployment based on operational objectives.

Problem Statement

Late deliveries negatively impact:

Customer satisfaction

Operational efficiency

Cost management

The objective of this project is to identify delayed shipments using predictive modeling while carefully balancing precision and recall according to business risk tolerance.

Dataset and Data Splitting

80 percent Training Data

20 percent Testing Data

Stratified sampling applied to maintain class distribution

Evaluation Metrics

Models were evaluated using:

Accuracy

Precision

Recall

F1 Score

ROC-AUC

Confusion Matrix

Classification Report

These metrics were selected to measure both predictive performance and real-world operational impact.

Model Development and Comparison

Logistic Regression (Baseline)

Hyperparameter tuning performed using GridSearchCV

Performance:

Accuracy: 69.15 percent

Precision: 84.3 percent

Recall: 53.8 percent

F1 Score: 0.656

ROC-AUC: 0.740

Insight:

High precision

Moderate recall

Establishes baseline performance

Logistic Regression (Feature Engineered)

Engineered Features:

urgency_ratio

profit_margin

discount_effect

geo_interaction

Performance:

Accuracy: 69.12 percent

Precision: 84.2 percent

Recall: 53.7 percent

F1 Score: 0.656

ROC-AUC: 0.740

Insight:

No significant improvement over baseline

Suggests nonlinear relationships within the dataset

Random Forest (Tuned)

Configuration:

250 trees

Maximum depth: 20

Class balancing applied

Performance:

Accuracy: 69.58 percent

Precision: 83.6 percent

Recall: 55.4 percent

F1 Score: 0.666

ROC-AUC: 0.767

Insight:

Improved nonlinear pattern capture

Slight improvement in recall and ROC-AUC

XGBoost (Threshold Optimized)

Decision threshold tuned to maximize F1 score

Optimized for higher recall

Performance:

Accuracy: 66.56 percent

Precision: 65.4 percent

Recall: 82.9 percent

F1 Score: 0.731

ROC-AUC: 0.775

Insight:

Highest recall among all models

Suitable for risk-sensitive deployment

Captures majority of late deliveries

XGBoost (Advanced Feature Engineering – Final Tuned Model)

Additional Engineered Features:

urgency_ratio

profit_margin

discount_effect

price_per_quantity

shipment_pressure

Model Configuration:

n_estimators: 400

max_depth: 5

learning_rate: 0.05

subsample: 0.9

colsample_bytree: 0.9

scale_pos_weight for class imbalance

eval_metric: logloss

Performance:

ROC-AUC: 76.95 percent

Accuracy: 70.02 percent

Precision: 84.67 percent

Recall: 55.34 percent

F1 Score: 66.93 percent

Confusion Matrix:

True Negatives: 14325

False Positives: 1983

False Negatives: 8841

True Positives: 10955

Insight:

Highest overall accuracy

Strong precision

Stable and balanced performance

Final Model Selection

The advanced feature-engineered XGBoost model was selected as the final deployed model due to:

Highest accuracy

Strong precision

Competitive ROC-AUC

Balanced and stable performance

The trained model was saved as:

xgb_supply_chain_model.pkl

Workflow Automation

The pipeline is automated using Apache Airflow to orchestrate:

Data loading

Feature engineering

Model training

Model evaluation

Model artifact storage

This ensures reproducibility, scalability, and production readiness.

Technology Stack

Python

Pandas

NumPy

Scikit-learn

XGBoost

Matplotlib

Joblib

Apache Airflow