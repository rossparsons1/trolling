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

# 2. Интеграционный

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

# 6. Параметризованный
