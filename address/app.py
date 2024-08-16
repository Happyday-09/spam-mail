from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# 모델 로드
model = joblib.load('spam_detector_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def index():
    return render_template('page.html')  # HTML 파일 경로를 맞춰야 합니다.

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        email_content = data['message']
    
        # 벡터화
        email_vectorized = vectorizer.transform([email_content])
    
        # 예측
        spam_prediction = model.predict(email_vectorized)
    
        return jsonify({'spam': bool(spam_prediction[0])})
    except Exception as e:
        return jsonify({'error' : str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)