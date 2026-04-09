from flask import Flask, render_template, request
from feature_extraction import extract_features, explain_url
from model import model, accuracy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

history = []

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']

    # Extract features
    features = [extract_features(url)]

    # Prediction
    prediction = model.predict(features)

    # 🔥 ADD THIS LINE (confidence)
    confidence = model.predict_proba(features)[0]

    confidence_score = max(confidence)   # highest probability

    # Result
    if prediction[0] == 1:
        result = "⚠️ Phishing URL"
        color = "red"
    else:
        result = "✅ Safe URL"
        color = "green"

    return render_template(
        'index.html',
        prediction_text=result,
        color=color,
        confidence=round(confidence_score * 100, 2)
    )
if __name__ == "__main__":
    print("Starting Flask server...")   # <-- add this line
    app.run(debug=True)
