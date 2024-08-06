while True:
    a = int(input('напишіть число'))
    operation = input('введіть операцію: +, -, *, /')
    b = int(input('напишіть друге число'))
    if operation == '+':
        result = (a + b)
        print(result)
        if operation == '-':
            result = (a - b)
            print(result)
            if operation == '*':
                result = (a * b)
                print(result)
            elif operation == '/':
                if b != 0:
                    print(a / b)
    else:
        print('Ділення на нуль')
        break
    if input("Для продовження операцій натисніть'y'?") != "y":
        break






