a = (input("")[:140])
a = a.title()
a = a.replace(' ', '').replace('', '').replace('&', '').replace('#', '').replace('"', '').replace('~', '').replace('%', '').replace('$', '').replace('@', '').replace('*', '').replace('.', '').replace('?', '').replace('&', '').replace('!', '').replace(',', '')

print('#' + a)
