# охотники за сокровищами

import random
import sys
import math

def getNewBoard():
    # Создать структуру данных нового игрового поля размером 60х15.
    board = []
    for x in range(60): # ...
        board.append([])
        for y in range(15): # ...
        # ...
            if random.randint(0,1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board):
    # ...
    tensDigitsLine = ' '
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    # ...
    print(tensDigitsLine)
    print(' ' + ('0123456789' * 6))
    print()

    # ...
    for row in range(15):
        # ...
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

        # ...
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    # ...
    print()
    print('   ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):
    # ...
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests: # ...
            chests.append(newChest)
    return chests

def isOnBoard(x, y):
    # ...
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    # ...
    # ...
    # ...
    smallestDistance = 100 # ...
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

        if distance < smallestDistance: # ...
            smallestDistance = distance

        smallestDistance = round(smallestDistance)

        if smallestDistance == 0:
            # ...
            chests.remove([x, y])
            return 'Вы нашли сундук с сокровищами на затонувшем судне!'
        else:
            if smallestDistance < 10:
                board[x][y] = str(smallestDistance)
                return 'Сундук с сокровищ. обнаружен на растоянии %s от гидролокатора.' % (smallestDistance)
            else:
                board[x][y] = 'X'
                return 'Гидролокатор ничего не обнаружил. Все сундуки с сокров. вне досягаемости.'

def enterPlayerMove(previousMoves):
    # ...
    print('Где следует опустить гидролокатор? (коорд.: 0-59 0-14) (или ввкдите "выход")')
    while True:
        move = input()
        if move.lower() == 'выход' or move.lower() == 'exit':
            print('Спасибо за тгру!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('Здесь вы уже опускали гидролокатор.')
                continue
            return [int(move[0]), int(move[1])]

    print('Введите число от 0 до 59, потом пробел, а затем число от 0 до 14.')

def showInstructions():
    print('''Инструктаж:
    Вы - капитан корабля, плывущего за сокровищами. Ваша задача - с помощью
    гидролокатора найти три сундука с сокровищ. в затонувших суднах на дне океана.
    Но гидролокаторы очень просты и определяют только расстояние, но не направление.
    Введите коорд-ы, чтобы опустить ГЛ в воду. На карте будет показано
    число, обозначающее, на каком расстоянии находится ближ. сундук. Или будет
    показана буква Х, обозначающая, что сундук в области действия ГЛ не
    обнаружен. На карте ниже метки С - это сундуки.
    Цифра 3 обозначает, что ближ. сундук наход. на отдалении в 3 единицы.
    
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
    (Во время игры сундуки на карте не обозначаются!)
    
    Нажмите клавишу Enter, чтобы продолжить...''')
    input()

    print('''Если ГЛ опущен прямо на сундук, вы сможете поднять
    сундук. Другие ГЛ обновят данные о расположении ближ сундука.
    Сундуки ниже находятся вне диапазона ГЛ, поэтому отображ. буква Х.
    
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
    Сундуки с сокров. не перемещаются. ГЛ определяют сундуки
    на расстоянии до 9 единиц. Попробуйте поднять все 3 сундука до того, как вск
    ГЛ будут опущены на дно. Удачи!
    
    Нажмите клавишу Enter, чтобы продолжить...''')
    input()



print('Охотник за сокровищами!')
print()
print('Показать инструктаж? (да/нет)')
if input().lower().startswith('д') or input().lower().startswith('y'):
    showInstructions()

while True:
    # ...
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        # ...
        print('Осталось ГЛ: %s. Осталось сундуков: %s.' % (sonarDevices, len(theChests)))

        x, y = enterPlayerMove(previousMoves)
        previousMoves.append([x, y]) # ...

        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
            if moveResult == 'Вы нашли сундук с сокровищами на затонувшем судне!':
                # ...
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)

        if len(theChests) == 0:
            print('Вы нашли все сундуки на затонувших суднах! Поздравляем и приятной игры!')
            break

        sonarDevices -= 1

    if sonarDevices == 0:
        print('Все ГЛ опущены на дно! Придется разварачивать корабль и')
        print('отправляться домой, в порт! Игра окончена.')
        print('Вы не нашли сундуки в след. местах:')
        for x, y in theChests:
            print(' %s, %s' % (x, y))

    print('Хотите сыграть еще раз? (да или нет)')
    if not input().lower().startswith('д') or not input().lower().startswith('y'):
        sys.exit()