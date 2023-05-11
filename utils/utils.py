import json
import os
from datetime import datetime


filepath = os.path.join(os.path.dirname(__file__), '..', 'operations.json')
def open_json(value):
    with open(value, 'r', encoding="utf-8") as f:
        file = f.read()
        operations = json.loads(file)
        return operations


def state_executed():
    operations = open_json(filepath)
    sorted_operations = sorted(operations, key=lambda op: op.get('date', ''), reverse=True)
    result = []
    count = 0
    for name in sorted_operations:
        if name.get("state") == "EXECUTED":
            # перевод даты в нужный формат
            DATE = name['date'][:10]
            date = datetime.strptime(DATE, "%Y-%m-%d")
            correct_date = datetime.strftime(date, "%d.%m.%Y")

            # маскировка номер карты в поле "from"
            corect_from = name.get("from")
            if corect_from != None:
                corect_from = corect_from.split(" ")
                corect_from = ' '.join(corect_from[:-1]) + ' ' + (corect_from[-1][:4] + '** **** ' + corect_from[-1][-4:])
            elif corect_from == None:
                corect_from = "no sender account "
            # маскировка номер карты в поле "to"
            correct_to = name["to"].split()
            correct_to = correct_to[0] + " **" + correct_to[1][-4:]
            # сумма перевода и валюта
            sum_operationAmount = name['operationAmount']['amount'] + " " + name['operationAmount']['currency']['name']
            result.append(f'{correct_date} {name["description"]}\n'
                          f'{corect_from} -> {correct_to}\n'
                          f'{sum_operationAmount}\n'
                          f'\n')
            count += 1
            if count == 5:
                break
    return ''.join(result)








