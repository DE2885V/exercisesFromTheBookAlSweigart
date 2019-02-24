import random

guessesTaken = 0

print ('Hi! What is yr name?')

myName = input()

number = random.randint(1, 20)
print ('Что ж, ' + myName + ', я загадываю число от 1 до 20.')


for guessesTaken in range(6):
    print ('Попробуй угадать.')
    guess = int(input())

    if guess < number:
        print ('Твое число слишком маленькое.')
    
    if guess > number:
        print ('Твое число слишком большое.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print ('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')

if guess != number:
    number = str(number)
    print ('Увы. Я загадала число ' + number + '.')
