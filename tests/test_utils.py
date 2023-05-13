import os
from utils.utils import state_executed, get_data, get_operationAmount, get_description, get_from, get_to, open_json



filepath = os.path.join(os.path.dirname(__file__), '..', 'operations.json')
OPEN = open_json(filepath)
START = state_executed()
DATA = get_data()
OPERATION = get_operationAmount()
DESCRIPTION = get_description()
FROM = get_from()
TO = get_to()

def test_OPEN():
    # проверка на то, что функций не возвращает значение None
    assert open_json(filepath) != None
    # проверка на то, что функций  возвращает список
    assert isinstance(open_json(filepath), list)
def test_START():
    # проверка на то, что функция проходит не более 5 итераций
    assert len(START) <= 5
    # проверка на то, что функция возвращает список
    assert isinstance(START, list)
    # проверка на то, что список функции добавляет не пустые значения
    for i in range(5):
        assert START[i] != None
def test_DATA():
    # проверка на то, что функция проходит не более 5 итераций
    assert len(DATA) <= 5
    # проверка на то, что функция возвращает список
    assert isinstance(DATA, list)
    # проверка на то, что список функции добавляет не пустые значения
    for i in range(5):
        assert DATA[i] != None
def test_OPERATION():
    # проверка на то, что функция проходит не более 5 итераций
    assert len(OPERATION) <= 5
    # проверка на то, что функция возвращает список
    assert isinstance(OPERATION, list)
    # проверка на то, что список функции добавляет не пустые значения
    for i in range(5):
        assert OPERATION[i] != None
def test_DESCRIPTION():
    # проверка на то, что функция проходит не более 5 итераций
    assert len(DESCRIPTION) <= 5
    # проверка на то, что функция возвращает список
    assert isinstance(DESCRIPTION, list)
    # проверка на то, что список функции добавляет не пустые значения
    for i in range(5):
        assert DESCRIPTION[i] != None
def test_FROM():
    # проверка на то, что функция проходит не более 5 итераций
    assert len(FROM) <= 5
    # проверка на то, что функция возвращает список
    assert isinstance(FROM, list)
    # проверка на то, что список функции добавляет не пустые значения
    for i in range(5):
        assert FROM[i] != None
def test_TO():
    # проверка на то, что функция проходит не более 5 итераций
    assert len(TO) <= 5
    # проверка на то, что функция возвращает список
    assert isinstance(TO, list)
    # проверка на то, что список функции добавляет не пустые значения
    for i in range(5):
        assert TO[i] != None


