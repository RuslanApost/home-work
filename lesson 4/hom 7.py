lok = [1, 2, 3, 0, 5, 7, 0, 4, 6, 8, 5, 8, 0, 9, 6, 0, 1]
a = 0
for a in range(len(lok) - 1):
    if lok[a] == 0:
        lok.append(lok.pop(a))
print(lok)