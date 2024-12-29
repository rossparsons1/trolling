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

# 4. Приемочные

# 5. Нагрузочный

# 6. Параметризованный