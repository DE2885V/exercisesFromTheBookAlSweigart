import random
print(
    '''Я подброшу монетку 1000 раз.
Угадай, сколько раз выпадет "Орел"?
(Нажми клавишу Enter, чтобы начать)'''
)
input()
flips = 0
heads = 0

while flips < 1000:
    if random.randint(0, 1) == 1:
        heads += 1

    flips += 1
    
    if flips == 900:
        print('900 подкидываний и "Орел" выпал ' + str(heads) + 'раз. ' + str(heads * 100 / 1000) + '%')
    if flips == 100:
        print('100 подкидываний и "Орел" выпал ' + str(heads) + 'раз. '+ str(heads * 100 / 1000) + '%')
    if flips == 500:
        print('500 подкидываний и "Орел" выпал ' + str(heads) + 'раз. '+ str(heads * 100 / 1000) + '%')

print()
print('Из 1000 подбрасываний монетки "Орел" выпал ' + str(heads) + ' раз! '+ str(heads * 100 / 1000) + '%')
print('Насколько вы близки к правильному ответу')
