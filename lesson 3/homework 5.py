list1 = [10, 7, 4, 8, 9, 5]
list2 = []
if list1 <= list2:
    print([])
elif list1 != list2:
    list2 = list1.pop()
    list1.insert(0, list2)
    print(list1)
