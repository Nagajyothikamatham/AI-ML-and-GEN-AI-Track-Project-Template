import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib
import os

# Load dataset
data = pd.read_csv("dataset/flood.csv")

# Features and Target
X = data.drop("FloodProbability", axis=1)
y = data["FloodProbability"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
score = r2_score(y_test, y_pred)

print("Model Accuracy (R2 Score):", score)

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save Model
joblib.dump(model, "model/flood_model.pkl")

print("Model saved successfully!")