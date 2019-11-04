from RegularMachine import RegularMachine
from LongestSuffix import longest_suffix

if __name__ == '__main__':
    while(True):
        print("Введите через Enter две строки: регулярное выражение и слово u.\n"
              "Для выхода введите Exit")
        regular_machine_str = input()
        if regular_machine_str == "Exit":
            exit()
        pattern = input()
        result = longest_suffix(regular_machine_str, pattern)
        print(result)