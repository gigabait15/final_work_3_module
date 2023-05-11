import os
from datetime import datetime
from utils.utils import open_json, state_executed


file = os.path.join(os.path.dirname(__file__), '..', 'test_json.json')
filepath = os.path.join(os.path.dirname(__file__), '..', 'operations.json')
def test_open_json():
    # Проверяем, что функция возвращает список
    assert isinstance(open_json(filepath), list)
    # проверка на возвращение корректных данных для пустого списка операций
    assert open_json(file) == []

def test_state_executed():
    # Проверяем, что функция возвращает строку
    assert isinstance(state_executed(), str)
    # проверка на количество возвращаемых транзакций
    assert state_executed().count("\n\n") == 5


