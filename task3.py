from random import randint

s = input('Enter word: ')
dlina = len(s) - 1
for j in range (0,5,1):
    i = 0
    while i <= dlina - 1:
        rnd = randint(i + 1, dlina)
        sss = s[i]
        ss = s.replace(s[i], s[rnd], 1)
        del s
        temp=ss[i+1:]
        s = ss[:i+1]+temp.replace(temp[rnd-i-1], sss, 1)
        i += 1
    print(f'New word: {s}')
