# -*- coding: utf-8 -*-
"""FinalMachineLearningProject.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mbMWODA7KSRE18PrrlQSOg1EaBBRfkKO
"""

!pip install shap -q


import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split


from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import ExtraTreesRegressor
import joblib
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.stats as stats
import plotly.graph_objects as go
import plotly.express as px
from scipy.stats import spearmanr
from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform

# Import filters to remove unnecessary warnings
from warnings import simplefilter
import warnings
warnings.filterwarnings("ignore")
from sklearn.exceptions import ConvergenceWarning

from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform

# Import filters to remove unnecessary warnings
from warnings import simplefilter
import warnings
warnings.filterwarnings("ignore")

from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score, mean_absolute_error
import shap

"""Above are all of my neccesary libraries I need to download for this project, eventually when I expand beyond comparitive analaysis of DNA sequences and how effective their start and stop codons are at creating neccesary genomes I will expand this list.

"""

# load the data
df=pd.read_excel("/content/yeastexcel.xlsx")

# check if the data contains null values
df.isna().sum()

"""The above dataset is different yeast genomes and how likely they are to create and reproduce itself.  This dataset is aspecficially a yeast based one."""

#Check data for general info
df.info()

"""Above is the info command for the dataset"""

# Check for duplicates in the entire dataset
duplicates = df.duplicated()
# If there are any duplicates, the 'duplicates' variable will contain True for those rows
if duplicates.any():
    # Get the rows with duplicates
    duplicate_rows = df[duplicates]
else:
    print("No duplicates found in the dataset.")

"""The above lines check for duplicated data in the data sets"""

# drop duplicates
data = df.drop_duplicates()

"""This line drops the duplicate data

PREPROCESSING
"""

!pip install pandas numpy
import pandas as pd
import numpy as np

def replace_words_with_mean(df):
    """
    Replaces non-numeric values in a DataFrame with the column mean.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with non-numeric values replaced by column means.
    """
    for column in df.select_dtypes(include=['number']).columns:  # Iterate through numeric columns
        # Convert to numeric, errors='coerce' will turn non-numeric values to NaN
        df[column] = pd.to_numeric(df[column], errors='coerce')

        # Calculate mean of numeric values, ignoring NaNs
        column_mean = df[column].dropna().mean()

        # Replace NaNs (which were originally non-numeric) with the mean
        df[column] = df[column].fillna(column_mean)

    return df

# Assuming 'data' is your DataFrame
data_cleaned = replace_words_with_mean(data.copy())  # Use a copy to avoid modifying the original DataFrame

# Now you can use data_cleaned for your model training

"""This command drops all none number values in the dataset to clean the dataset as a whole"""

data.describe()  # Summary statistics for numerical columns

data['mcg'].unique()

data['mcg'].value_counts() # number of occurence of each unique value

"""I will be specifically evaluating the mcg section of the dataset as it holds the most output values of all the other columns."""

# Assuming 'data' is your DataFrame
data = data.drop('name', axis=1)

sns.pairplot(data)

"""Above is a pairplot of all the data against eachother and each value."""

# Convert specific columns to numeric, handling errors
for column in df.select_dtypes(include=['object']).columns:
    try:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    except ValueError:
        print(f"Could not convert column '{column}' to numeric. It likely contains non-numeric strings.")

# Calculate the correlation matrix only on numeric columns
correlation_matrix = df.select_dtypes(include=np.number).corr()

# Print the correlation matrix
print(correlation_matrix)

"""Above is a correlation table telling us how the data stacks against eachother.  For this dataset there us very little correlation between values if at all which posses problems for us in the future.

MACHINE LEARNING SECTION
"""

from sklearn.model_selection import train_test_split

X = data[['mcg']]
y = data['nuc']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)#### Data Cleansing

from sklearn.model_selection import train_test_split

X = data[['mcg']]
y = data['nuc']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

"""The above line setups the test-train split for this dataset and can set up the rest of the project goals."""

from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()
linear_regression.fit(X = X_train, y = y_train)

"""This line specifically allows for linear regression models to be used."""

print('β1 = ' + str(linear_regression.coef_) + ', β0 = ' + str(linear_regression.intercept_))

"""These values are the regression coefficients for the overall linear regression equation."""

from sklearn.metrics import r2_score
y_pred_test = linear_regression.predict(X_test)
y_pred_train = linear_regression.predict(X_train)

print('R2 train = ', r2_score(y_train, y_pred_train))
print('R2 test = ', r2_score(y_test, y_pred_test))

"""Very low correlation found in this dataset, will be hard to produce good machine learning outcomes from this."""

plt.scatter(y_train,y_pred_train, label='Training Set')
plt.scatter(y_test,y_pred_test, label='Test Set')
plt.xlabel('Real')
plt.ylabel('Predicted')
plt.legend()
plt.show()

"""Above is the training set vs the predicted set, as viewed the test set is a lot more clustered than the training set which is to be expected."""

from sklearn.model_selection import train_test_split

X = df.drop(['mcg', 'nuc'], axis=1)
y = df['nuc']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

from sklearn import preprocessing

scaler = preprocessing.StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

"""Another minor preprocessing is done here to to preform test training split."""

!pip install sklearn
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
# ... (your existing code for loading data and defining X, y) ...

# Create an imputer to replace NaN with the mean of the column
imputer = SimpleImputer(strategy='mean')

# Fit the imputer on the training data and transform both training and testing data
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Now you can proceed with fitting the model
multiple_linear_regression = LinearRegression()
multiple_linear_regression.fit(X = X_train, y = y_train)

"""Again we are fitting this training data for linear regression modelling."""

from sklearn.metrics import mean_squared_error, r2_score

y_pred = multiple_linear_regression.predict(X_test)

rmse_MLR = np.sqrt(mean_squared_error(y_test, y_pred))

r2 = r2_score(y_test, y_pred)

print('R2 test = ', r2)
print('RSME test = ', rmse_MLR)

"""RSME test shows to be a lot more effective than the R2 tests.  Both are still incredibly low and will not produce good results, with better data of course.

MACHINE LEARNING PORTION
"""

!pip install sklearn
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.model_selection import train_test_split

# Create an imputer to replace NaN with the mean of the column
imputer = SimpleImputer(strategy='mean')

# Fit the imputer on the training data and transform both training and testing data
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

X = data.drop('mcg',axis=1)
Y = data['mcg']
# Select only numerical columns (excluding 'object' type)
X = X.select_dtypes(exclude=['object'])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialize models
models = {
    'SGD': SGDRegressor(),
    'Random Forest': RandomForestRegressor(),
    'Gradient Boosting': GradientBoostingRegressor(),
    'AdaBoost': AdaBoostRegressor(),
    'Decision Tree': DecisionTreeRegressor(),
    'MLP': MLPRegressor(),
    'SVR': SVR(),
    'XGBoost': XGBRegressor(),
    'Linear Regression': LinearRegression(),
    'Extra Trees': ExtraTreesRegressor()
}

# Train and evaluate each model
for name, model in models.items():
    # Impute missing values before fitting for models that require it
    if name in ['SGD', 'Linear Regression', 'MLP', 'SVR']: # Add other models that may require imputation
        model.fit(imputer.fit_transform(X_train), y_train) # Fit imputer on X_train and transform
        y_pred = model.predict(imputer.transform(X_test)) # Transform X_test using fitted imputer
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

# Train and evaluate each model
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"{name} Mean Squared Error: {mse:.3f}, R² Score: {r2:.3f}, MAE: {mae:.3f}")
    print(' ')

"""The above intiilizies all machine learning models for comparison.  Only a few prove at all comperable for developing models around."""

# Initialize the StandardScaler
scaler = StandardScaler()

# Scale the training and testing data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize models
models = {
    'SGD': SGDRegressor(),
    'Random Forest': RandomForestRegressor(),
    'Gradient Boosting': GradientBoostingRegressor(),
    'AdaBoost': AdaBoostRegressor(),
    'Decision Tree': DecisionTreeRegressor(),
    'MLP': MLPRegressor(),
    'SVR': SVR(),
    'XGBoost': XGBRegressor(),
    'Linear Regression': LinearRegression(),
    'Extra Trees': ExtraTreesRegressor()
}

# Train and evaluate each model
for name, model in models.items():
    model.fit(X_train_scaled, y_train)  # Train with scaled data
    y_pred = model.predict(X_test_scaled)  # Predict with scaled test data
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"{name} Mean Squared Error: {mse:.3f}, R² Score: {r2:.3f}, MAE: {mae:.3f}")
    print(' ')

"""The above line is above standardization, again this almost makes the modelling worse."""

# Apply one-hot encoding to specific columns
encoded_df = pd.get_dummies(data, columns=['mcg'])
x = encoded_df.drop('nuc',axis=1)
y = encoded_df['nuc']
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

# Initialize models
models = {
    'SGD': SGDRegressor(),
    'Random Forest': RandomForestRegressor(),
    'Gradient Boosting': GradientBoostingRegressor(),
    'AdaBoost': AdaBoostRegressor(),
    'Decision Tree': DecisionTreeRegressor(),
    'MLP': MLPRegressor(),
    'SVR': SVR(),
    'XGBoost': XGBRegressor(),
    'Linear Regression': LinearRegression(),
    'Extra Trees': ExtraTreesRegressor()
}

# Train and evaluate each model
selected_models = []
for name, model in models.items():
    model.fit(X_train, y_train)  # Train with scaled data
    y_pred = model.predict(X_test)  # Predict with scaled test data
    r2 = r2_score(y_test, y_pred)
    if r2 > 0.90:
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        print(f"{name} R² Score: {r2:.3f}, Mean Squared Error: {mse:.3f}, MAE: {mae:.3f}")
        print(' ')
        selected_models.append((name, model))

"""This code does not work for my dataset as nmone of my R2 values are above .9.

Cross Validation
"""

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

 # Initialize models
models = {
    'SGD': SGDRegressor(),
    'Random Forest': RandomForestRegressor(),
    'Gradient Boosting': GradientBoostingRegressor(),
    'AdaBoost': AdaBoostRegressor(),
    'Decision Tree': DecisionTreeRegressor(),
    'MLP': MLPRegressor(),
    'SVR': SVR(),
    'XGBoost': XGBRegressor(),
    'Linear Regression': LinearRegression(),
    'Extra Trees': ExtraTreesRegressor()
}

# Cross-validation for each model
selected_models = []
for name, model in models.items():
    cv_scores = cross_val_score(model, x, y, cv=10, scoring='r2')  # Perform 5-fold cross-validation
    mean_r2 = cv_scores.mean()
    if mean_r2 > 0.1:
        print(cv_scores,model)
        model.fit(X_train, y_train)  # Train the model on the entire training set
        y_pred = model.predict(X_test)  # Predict on the test set
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        print(f"{name} Mean R² Score: {mean_r2:.3f}, Mean Squared Error: {mse:.3f}, MAE: {mae:.3f}")
        print('mcg')
        selected_models.append((name, model))

"""This above code is to describe the cross validation for the model in general."""

# Split the dataset into training and testing sets
X = data.drop('mcg',axis=1)
Y = data['mcg']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

# Initialize the StandardScaler for numerical columns and OneHotEncoder for categorical columns
numerical_features = X_train.select_dtypes(exclude=['object']).columns
categorical_features = ['nuc']  # Replace 'Location' with your categorical column name
encoder = OneHotEncoder()

# Feature transformation function for log, square root, and polynomial features
log_sqrt_transformer = FunctionTransformer(np.log1p, validate=True)
polynomial_transformer = PolynomialFeatures(degree=2, include_bias=False)

# Create a ColumnTransformer to handle preprocessing for both numerical and categorical features
preprocessor = ColumnTransformer(
    transformers=[
     ('log_sqrt',log_sqrt_transformer,numerical_features),
       ('poly_trans',polynomial_transformer,numerical_features),
        ('cat', encoder, categorical_features)
    ]
)
# Initialize models
models = {
   'SGD': SGDRegressor(),
  'Random Forest': RandomForestRegressor(),
   'Gradient Boosting': GradientBoostingRegressor(),
   'AdaBoost': AdaBoostRegressor(),
    'Decision Tree': DecisionTreeRegressor(),
    'MLP': MLPRegressor(),
    'SVR': SVR(),
    'XGBoost': XGBRegressor(),
    'Linear Regression': LinearRegression(),
   'Extra Trees': ExtraTreesRegressor()
}


# Train and evaluate each model
for name, model in models.items():
    # Use Pipeline to chain preprocessing and modeling steps
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', model)
    ])

    model_pipeline.fit(X_train, y_train)  # Train the model

"""This is to describe all of the machine learning models"""

def plot_correlation(data,target_column='mcg'):
  """
  Function that shows the correlation and clustering between the features:
  """

  # Create a copy of the data to avoid modifying the original DataFrame
  df = data.copy()

  # Convert 'mcg' column to dummy variables
  df = pd.get_dummies(df, columns=['mcg'], prefix='mcg')

  # Define the columns to drop (original 'mcg' column is not present anymore)
  columns_to_drop = [col for col in df.columns if col.startswith('mcg_')] + [target_column] # Assuming you want to drop the target column
                                                                                                     # and all dummy columns created from it
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))
  corr = spearmanr(x).correlation

  # Ensure the correlation matrix is symmetric
  corr = (corr + corr.T) / 2
  np.fill_diagonal(corr, 1)
  # We convert the correlation matrix to a distance matrix before performing
  # hierarchical clustering using Ward's linkage.
  distance_matrix = 1 - np.abs(corr)
  dist_linkage = hierarchy.ward(squareform(distance_matrix))
  dendro = hierarchy.dendrogram(
      dist_linkage, ax=ax1, leaf_rotation=90
  )
  dendro_idx = np.arange(0, len(dendro["ivl"]))

  ax2.imshow(corr[dendro["leaves"], :][:, dendro["leaves"]])
  ax2.set_xticks(dendro_idx)
  ax2.set_yticks(dendro_idx)
  ax2.set_xticklabels(dendro["ivl"], rotation="vertical")
  ax2.set_yticklabels(dendro["ivl"])
  fig.tight_layout()
  plt.show()

plot_correlation(data)

"""Above is a correlation plot for the entire dataset and it does not really tell us a lot."""

def plot_shap(data, target_column, model):
    """
    Plots SHAP summary plot for a given model and dataset.

    Args:
        data (pd.DataFrame): The input dataset.
        target_column (str): The name of the target column.
        model: The trained machine learning model.
    """
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    # Fit the model before using it in the explainer
    model.fit(X, y)  # Train the model before calculating SHAP values

    # Create object that can calculate shap values
    explainer = shap.Explainer(model)

    # Calculate Shap values
    shap_values = explainer(X)

    # Summary plot
    shap.summary_plot(shap_values, X)
    plt.show()

# Assuming you have already defined 'data', 'mcg', and 'model'
# define model to use
model = GradientBoostingRegressor()
plot_shap(data,'mcg',model)