# tests/test_main.py
from app.main import hello

def test_hello():
    assert hello() == "Hello, World!"

