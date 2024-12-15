# utilities
import re
import numpy as np
import pandas as pd
import csv
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from joblib import dump, load

X_train_resampled=pd.read_csv('X_train_resampled.csv').reset_index(drop=True)

print(X_train_resampled.shape)
print(X_train_resampled.info())
y_train_resampled = pd.read_csv("y_train_resampled.csv").reset_index(drop=True)
print(y_train_resampled.shape)
print(y_train_resampled.info())
X_val = pd.read_csv("X_val.csv").reset_index(drop=True)
y_val = pd.read_csv("y_val.csv").reset_index(drop=True)


#baseline_model = LogisticRegression(multi_class="multinomial", solver="lbfgs", max_iter=500, random_state=42)
#penalty='l2', C=0.1
baseline_lr_model = LogisticRegression(
    multi_class="multinomial", solver="lbfgs", max_iter=1000, random_state=42, class_weight="balanced", penalty='l2', C=0.1
)
baseline_lr_model.fit(X_train_resampled, y_train_resampled)

print("\n Done training--------------------\n")

# Evaluate baseline model on validation set
y_val_pred_baseline = baseline_lr_model.predict(X_val)
print("Baseline Model Accuracy (Validation):", accuracy_score(y_val, y_val_pred_baseline))
print(classification_report(y_val, y_val_pred_baseline, target_names={'A': 0, 'B': 1, 'C': 2, 'N': 4}))


# Save the model
dump(baseline_lr_model, 'rf_model.joblib')