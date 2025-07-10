# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/heart.csv")

# Features and target
X = df.drop("target", axis=1)
y = df["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"✅ Model trained successfully! Accuracy: {accuracy:.2f}")

# Save model
joblib.dump(model, "models/heart_model.pkl")
print("✅ Model saved as models/heart_model.pkl")
