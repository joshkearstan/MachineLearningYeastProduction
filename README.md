# MachineLearningYeastProduction
Machine Learnign Project for Cheg 472
Problem Statement:
This project aims to evaluate the production of any genome to evaluate how well their dna analysis and their dna sequencing compares to others.

Input and Output Variables:
Inputs:
Different site structures of yeast (ex: mcg, hoc, gvh, etc) and all the associated preprocessing tasks within the code

Outputs:
Model Training and Evaluation: Trains various machine learning models, evaluates their performance using metrics like R-squared, MSE, and MAE, and selects the best-performing models.
Cross-Validation: Improves model reliability by assessing performance on multiple folds of the data.
Feature Preprocessing: Prepares data for modeling by handling numerical and categorical features (e.g., scaling, encoding).
Model Pipeline: Combines data preprocessing and model training into a single pipeline for efficient workflow.
Correlation Plot: Visualizes the relationships between features to identify potential correlations.
SHAP Explanations: Provides insights into the importance of features in making predictions, helping to understand the model's decision-making process.

Machine Learning Algorithm(s): 
SGD: Optimizes models iteratively using gradients.
Random Forest: Ensemble of decision trees for improved accuracy.
Gradient Boosting: Sequentially builds models to correct errors.
AdaBoost: Combines weak learners to create a strong model.
Decision Tree: Tree-like model for classification and regression.
MLP: Neural network with multiple layers.
SVR: SVM-based regression algorithm.
XGBoost: Efficient gradient boosting implementation.
Linear Regression: Models linear relationship between variables.
Extra Trees: Random forest with more randomness in tree construction.
  
Ethics Considerations:  My ethics datacard is in this repository labeled "Ethics Datacard"

Dataset:  Data used comes from https://biocyc.org/download.shtml  https://bioinformatics.ai.sri.com/ptools/ libraries
I used a basic yeast (yarrowia) dataset that analyzed the frequency of genomes and their dna sequencing
I specifically used this dataset from berkeley college about structure analsysis of yeast https://www.kaggle.com/datasets/samanemami/yeastcsv/data
