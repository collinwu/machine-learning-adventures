import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.externals import joblib

filepath = Path.cwd() / "machine-learning-adventures" / "linear_regression_training" / "data" / "house_data.csv"

datafile = pd.read_csv(filepath)

X = datafile[["sq_feet", "num_bedrooms", "num_bathrooms"]]
y = datafile["sale_price"]
