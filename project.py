import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

#data load
data = pd.read_csv() #csv file

#data preprocessing
X = data['message']
Y = data['label']

#train data and test data split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

#특성추출
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

#model learning
model = LogisticRegression()
model.fit(X_train_vectorized, Y_train)

#model evaluation
Y_pred = model.predict(X_test_vectorized)
accuracy = accuracy_score(Y_test, Y_pred)
precision = precision_score(Y_test, Y_pred, pos_label = 'spam')
recall = recall_score(Y_test, Y_pred, pos_label = 'spam')
f1 = f1_score(Y_test, Y_pred, pos_label = 'spam')

print('Accuracy : ', accuracy)
print('Precision : ', precision)
print('Recall : ', recall)
print('F1-score : ', f1)