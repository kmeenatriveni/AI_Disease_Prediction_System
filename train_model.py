import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Select features
X = data[['high_fever', 'headache', 'cough', 'vomiting', 'fatigue']]

# Target variable
y = data['prognosis']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save trained model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully and saved as model.pkl")
