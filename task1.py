from random import randint

while True:
    rnd = randint(0, 10)
    probe=input('Угадай число от 0 до 10  :')
    print(rnd)
    if rnd==probe:
        print('You win!!!')
    else:
        print('You loose')
    s=input("Next play(Y/N)")
    if s.lower()=="y":
        print('Next play')
    else:
        print('Good bay')
        break