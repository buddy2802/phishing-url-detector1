import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from feature_extraction import extract_features

# Load dataset
data = pd.read_csv("phishing.csv")

# Clean
data = data.dropna()
data = data.drop_duplicates()

# Features and labels
X = [extract_features(url) for url in data['url']]
y = data['label']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=100)

# Train
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)

print("Model Accuracy:", accuracy)