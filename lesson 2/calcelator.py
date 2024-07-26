a = int(input('напишіть число'))
operation = input('введіть операцію: +, -, *, /')
b = int(input('напишіть друге число'))
if operation == '+':
    result = (a + b)
    print(result)
elif operation == '-':
    result = (a - b)
    print(result)
elif operation == '*':
    result = (a * b)
    print(result)
elif operation == '/':
    result = (a / b)
    print(result)