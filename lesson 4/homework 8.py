import random
work = []
for i in range(random.randint(3, 10)):
    work.append(random.randint(1, 100))
print(work)
xum = (work [0])
cum = (work[2])
bum = (work[-2])
work = xum, cum, bum
print(work)