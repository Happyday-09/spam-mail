import pandas as pd
import joblib
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 데이터셋 로드
file_path = '/Users/hurkyeongjun/Desktop/spam data/SMSSpamCollection'
data = pd.read_csv(file_path, sep='\t', header=None, names=['label', 'message'])

# 레이블을 숫자로 변환
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# 텍스트 전처리 함수
def preprocess_text(text):
    text = text.lower()  # 소문자로 변환
    text = re.sub(r'\d+', '', text)  # 숫자 제거
    text = text.translate(str.maketrans('', '', string.punctuation))  # 구두점 제거
    return text

# 메시지 전처리
data['message'] = data['message'].apply(preprocess_text)

# 데이터셋 분할
X = data['message']
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 텍스트를 벡터화
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# 모델 학습
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# 모델 저장
joblib.dump(model, 'spam_detector_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')