from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# 모델 로드
model = joblib.load('spam_detector_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def index():
    return render_template('page.html')  # HTML 파일 경로를 맞춰야 합니다.

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    email_content = data['message']
    
    # 벡터화
    email_vectorized = vectorizer.transform([email_content])
    
    # 예측
    spam = model.predict(email_vectorized)
    
    return jsonify({'spam': bool(spam[0])})

if __name__ == '__main__':
    app.run(debug=True)