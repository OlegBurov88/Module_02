first = int(input('Введите 1-ое число: '))
second = int(input('Введите 2-ое число: '))
third = int(input('Введите 3-ье число: '))
if first == second and second == third :
    print(3)
elif first == second or first == third or second == third :
    print(2)
else:
    print(0)