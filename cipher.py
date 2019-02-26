# Шифр Цезаря
SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('зашифровать или расшифровать?')
        mode = input().lower()
        if mode in ['зашифровать', 'з', 'расшифровать','р']:
            return mode
        else:
            print('ВВедите "зашифровать" или "з" - "расшифровать" или "р"')

def getMessage():
    print('ВВедите текст:')
    return input()

def getKey():
    key = 0
    while True:
        print('Введите ключ шифрования (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'р':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: # ...
            # ...
            translated += symbol
        else:
            # ...
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated


mode = getMode()
message = getMessage()
key = getKey()
print('Преобразованный текст:')
print(getTranslatedMessage(mode, message, key))


if __name__ == '__main__':
    message = 'Это текст который нужно зашифровать'
    assert getTranslatedMessage('з', message, 15) == 'лБэ БущАБ щэБэяЙш ьВхьэ цоЖчГяэроБК'
    print ('assert Ok')
