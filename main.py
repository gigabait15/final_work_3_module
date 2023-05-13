from utils.utils import get_data, get_operationAmount, get_description, get_from, get_to


DATA = get_data()
OPERATION = get_operationAmount()
DESCRIPTION = get_description()
FROM = get_from()
TO = get_to()

def main():
    for i in range(5):
        print(f"{DATA[i]} {DESCRIPTION[i]}\n"
              f"{FROM[i]} -> {TO[i]}\n"
              f"{OPERATION[i]}\n")


if __name__ == "__main__":
    main()