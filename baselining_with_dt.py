# utilities
import re
import numpy as np
import pandas as pd
import csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score, ConfusionMatrixDisplay
from joblib import dump, load

X_train_resampled=pd.read_csv('X_train_resampled.csv').reset_index(drop=True)

print(X_train_resampled.shape)
y_train_resampled = pd.read_csv("y_train_resampled.csv").reset_index(drop=True)
print(y_train_resampled.shape)
X_val = pd.read_csv("X_val.csv").reset_index(drop=True)
y_val = pd.read_csv("y_val.csv").reset_index(drop=True)







# Initialize the Decision Tree model
dt_model = DecisionTreeClassifier(random_state=42)

# Train the model on training data
dt_model.fit(X_train_resampled, y_train_resampled)

################
print("Predict on validation set")
# Predict on validation set
y_val_pred = dt_model.predict(X_val)

# Evaluate model performance
print("Decision Tree Accuracy:", accuracy_score(y_val, y_val_pred))
print(classification_report(y_val, y_val_pred, target_names={'A': 0, 'B': 1, 'C': 2, 'N': 4}))


# Save the model
dump(dt_model, 'dt_baseline_model.joblib')
