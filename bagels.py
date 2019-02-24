import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    # Возвращ строку уникальных случайных цифр, длина которых составляет NUM_DIGITS.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Взвращ строку с подсказк. польз-ю "Тепло", "Горячо" и "Холодно".
    if guess == secretNum:
        return 'Вы угадали!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Горячо')
        elif guess[i] in secretNum:
            clues.append('Тепло')
    if len(clues) == 0:
        return 'Холодно'

    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    # ...
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


print('Я загадаю %s-х значное число, которое вы должны отгадать.' % (NUM_DIGITS))
print('Я дам несколько подсказок...')
print('Когда Я говорю: \t Это означает:')
print('  Холодно \t Ни одна цифра не отгадана.')
print('  Тепло \t Одна цифра отгадана, но не отгадана ее позиция.')
print('  Горячо \t Одна цифра и ее позиция отгаданы.')

while True:
    secretNum = getSecretNum()
    print('Итак, Я загадал число. У вас есть %s попыток, чтобы отгадать его.' % (MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Попытка №%s: ' % (guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('Попыток больше не осталось. Я загадал число %s.' % (secretNum))

    print('Хотите сыграть еще раз? (да или нет)')
    if not input().lower().startswith('д') or not input().lower().startswith('y'):
        break