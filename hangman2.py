import random
HANGMAN_PIC = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
    O |
      |
      |
     ===''', '''
  +---+
    O |
    | |
      |
     ===''', '''
  +---+
    O |
   /| |
      |
     ===''', '''
  +---+
    O |
   /|\|
      |
     ===''', '''
  +---+
    O |
   /|\|
   /  |
     ===''', '''
  +---+
    O |
   /|\|
   / \|
     ===''', '''
  +---+
   [O |
   /|\|
   / \|
     ===''', '''
  +---+
   [O]|
   /|\|
   / \|
     ===''']
words = {'Цвета'    :   'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),
        'Фигуры'    :   'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник шестиугольник восьмиугольник'.split(),
        'Фрукты'    :   'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split(),
        'Животные'  :   'аист акула бабуин баран барсук бобр бык верблюд волк вдоробей ворон выдра голубь гусь жаба зебра змея'.split()}

def getRandomWord(wordDict):
    # случайное слово из словаря списков строк, а также ключ.
    # во-первых, случайный ключ из словаря
    wordKey = random.choice(list(wordDict.keys()))

    # во-вторых, слово из списка ключей в словаре
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    
    return wordDict[wordKey][wordIndex], wordKey

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PIC[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #покащывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Возвращает букву, введенную игроком. Эта функция проверяет, что инрок ввел только одну букву и ничего больше
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess

def playAgain():
    #Эта функц. возвращ. Тру, если игрок хочет сыграть заново, иначе Фолс
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')

difficulty = ' '
while difficulty not in 'ЛСТ':
    print('Выберите ур. сложности: Л - легк., С - сред., Т - тяж.')
    difficulty = input().upper()
if difficulty == 'С':
    del HANGMAN_PIC[8]
    del HANGMAN_PIC[7]
if difficulty == 'Т':
    del HANGMAN_PIC[8]
    del HANGMAN_PIC[7]
    del HANGMAN_PIC[5]
    del HANGMAN_PIC[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False


while True:
    print('Секрктное слово из набора: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    #Позволяет игроку ввести букву.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #проверяет, выиграл ли игрок.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Да! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #Проверяет, превысил ли игрок лимит попыток и проиграл.
        if len(missedLetters) == len(HANGMAN_PIC) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерп. все попытки!\n'
                      'Не угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(len(correctLetters)) + ' Было загадано слово "' + secretWord + '".')
            gameIsDone = True
    # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
