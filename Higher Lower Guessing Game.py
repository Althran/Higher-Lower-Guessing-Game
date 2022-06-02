import random

game = 'y'
numbers_attempt = 0
win = 0
print('Hello, this is Higher Lower Guessing Game')
conceived_number = [i for i in range(0, 101)]
while game == 'y':
    computer = random.choice(conceived_number)

    while win == 0:
        print('Print your number')
        player = int(input())
        if player == computer:
            print('You win!, your numbers of attempts', numbers_attempt)
            win = 1
        elif player > computer:
            print('Your answer is higher than conceived number, try again')
        else:
            print('Your answer is lower than conceived number, try again')
        numbers_attempt += 1
    print('Another game?) y/n')
    game = input()
