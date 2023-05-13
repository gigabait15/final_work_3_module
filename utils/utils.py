import json
import os
from datetime import datetime


filepath = os.path.join(os.path.dirname(__file__), '..', 'operations.json')
def open_json(value):
    """
    открывает файл формата json и переводит его с список для дальнейшей работы
    :param value: исходный файл формата json
    :return:
    """
    with open(value, 'r', encoding="utf-8") as f:
        file = f.read()
        operations = json.loads(file)
        return operations


def state_executed():
    """
    открывает файл, сортирует по дате и сохранеяет в список первые пять отсортированных операций
    :return:
    """
    result = []
    operations = open_json(filepath)
    sorted_operations = sorted(operations, key=lambda op: op.get('date', ''), reverse=True)
    count = 0
    for name in sorted_operations:
        if name.get("state") == "EXECUTED":
            result.append(name)
            count += 1
            if count >= 5:
                break
    return result

def get_data():
    """
    перевод даты в нужный формат
    :return:
    """
    result = state_executed()
    correct_dates = []
    for item in result:
        DATE = item['date'][:10]
        date = datetime.strptime(DATE, "%Y-%m-%d")
        correct_date = datetime.strftime(date, "%d.%m.%Y")
        correct_dates.append(correct_date)
    return correct_dates

def get_operationAmount():
    """
    проходит по каждой итерации и сохраняет в список корректные данные п офинансам
    :return:
    """
    result = state_executed()
    correct_operationAmount = []
    for item in result:
        Amount = item['operationAmount']
        correct_Amount = Amount['amount'] + " " + Amount['currency']['name']
        correct_operationAmount.append(correct_Amount)
    return correct_operationAmount

def get_description():
    """
    возвращает описание (куда совершена транзакция) для каждой итерации
    :return:
    """
    result = state_executed()
    correct_description = []
    for item in result:
        description = item['description']
        correct_description.append(description)
    return correct_description

def get_from():
    """
    возвращаеет список с указаниями замаскированных карт отправителя,
    если их нет то сохраняет строку с предупреждением об отсутсвии данных отправителя
    :return:
    """
    result = state_executed()
    correct_from = []
    for item in result:
        FROM = item.get('from')
        if FROM is not None:
            FROM = FROM.split()
            FROM = FROM[0] + ' ' + FROM[-1][:4] + ' ' + FROM[-1][4:6] + '** **** ' + FROM[-1][-4:]
            correct_from.append(FROM)
        else:
            correct_from.append(f"нет данных отправителя")
    return correct_from

def get_to():
    """
    возвращаеет список с указаниями замаскированных счетов получателя
    :return:
    """
    result = state_executed()
    correct_to = []
    for item in result:
        TO = item['to'].split()
        correct_to.append(TO[0] + ' **' + TO[1][-4:])
    return correct_to





