import random

i = 0
a = input('enter word:')
while i <= 5:
    b = str(random.sample(a, len(a)))
    print(b[2:-2:5])
    i += 1
