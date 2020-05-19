# S = "Hello world!!!"
# word = input('Input stop word: ')
# print(S.replace(word, '***'))

g = 0
r = 0
while True:
    r = g
    o = int(input('введите чесло '))
    r = r + o
    if r < 1000:
       g = r
    if r > 1000:
        print('введите чесло меньше')
        print(f'чесло {1000-g}')

    if r == 1000:
        print(r)
        break
