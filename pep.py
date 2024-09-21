#import this

while 1 > 0:  # True
    number = int(input('Введите число: '))
    if number % 2 == 0:
        print('Число чётное')
        continue  # Начать цикл заново
    else:
        print('Число нечётное')
        break  # прерывание цикла
    print('Меня не забыли')  # строка не работает, т.к. цикл до ней не доходит
print('Я за циклом')