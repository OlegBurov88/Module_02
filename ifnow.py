name = input('Введите ваше имя: ')
if name == 'Oleg' :
    print('Здравствуйте, администратор')
else:
    print(f'Привет {name}')

number = int(input('Введите число: '))
if number % 3 == 0 and number % 5 == 0 :
    print('FizzBuzz')
elif number % 3 == 0 :
    print('Fizz')
elif number % 5 == 0 :
    print('Buzz')
else:
    print('Число не подходит')