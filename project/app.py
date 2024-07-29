from flask import Flask, request, jsonify, render_template
import joblib
import re
import string

app = Flask(__name__)

# model load
model = joblib.load('spam_detector_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# 전처리 함수
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

@app.route('/')
def home():
    return render_template('a.html') #HTML 파일 경로

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.json
    message = data['message']
    processsed_message = preprocess_text(message)
    
    # 벡터화 (사전에 학습한 CountVectorizer 사용)
    vectorized_message = vectorizer.transform([processsed_message])
    
    # 예측
    prediction = model.predict(vectorized_message)
    
    return jsonify({'spam' : bool(prediction[0])})

if __name__ == '__main__':
    app.run(debug = True)