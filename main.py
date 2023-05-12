from utils.utils import state_executed, filepath


def main():
    STATE = state_executed(filepath)
    print(STATE)

if __name__ == "__main__":
    main()