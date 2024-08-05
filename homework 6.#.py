a = (input("")[:140])
a = a.title()
while " " in a:
    a = a.replace(' ', '').replace('%', '').replace('$', '').replace('@', '').replace('*', '').replace('.', '').replace('?', '').replace('&', '').replace('!', '').replace(',', '')

print('#' + a)
