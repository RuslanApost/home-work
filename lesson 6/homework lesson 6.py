def multiply_digits(f):
    while f > 9:
        stage = 1
        for digit in str(f):
            stage *= int(digit)
        f = stage
    return f
numb = int(input("Введіть ціле число: "))
result = multiply_digits(numb)
print("Результат:", result)