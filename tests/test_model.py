import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import threading
from sklearn.feature_extraction.text import CountVectorizer
from fastapi.testclient import TestClient
from model import app, predict_toxicity

client = TestClient(app)

# 1. Модульный 
def test_vectorizer(): 
    vectorizer = CountVectorizer() 
    data = ["This is a test", "Another test"] 
    vectorized = vectorizer.fit_transform(data) 
    assert vectorized.shape == (2, 4) 
 
# 2. Интеграционный 
def test_api_predict(): 
    response = client.post("/predict/", json={"text": "Это ужасно!"}) 
    assert response.status_code == 200 
    assert "prediction" in response.json() 
    assert response.json()["prediction"] in ['Токсичный', 'Нетоксичный']

# 3. Регрессионный
def test_regression():
    test_cases = {
        "Это ужасно!": "Токсичный",
        "Все хорошо.": "Нетоксичный"
    }
    for comment, expected in test_cases.items():
        assert predict_toxicity(comment) == expected

# 4. Приемочные
def test_predict_toxicity():
    comment = "Это ужасно!"
    result = predict_toxicity(comment)
    assert result in ['Токсичный', 'Нетоксичный']

# 5. Нагрузочный
def test_load():
    def send_request():
        response = client.post("/predict/", json={"text": "Это ужасно!"})
        assert response.status_code == 200

    threads = []
    for _ in range(100):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# 6. Параметризованный
@pytest.mark.parametrize("input_text,expected", [
    ("Это ужасно!", "Токсичный"),
    ("Все хорошо.", "Нетоксичный"),
])
def test_predict_toxicity_param(input_text, expected):
    assert predict_toxicity(input_text) == expected
