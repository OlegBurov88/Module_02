import random


def say_hello():  # простая функция
    print('Hello')


say_hello()
say_hello()
say_hello()


def say_hello(name):  # принимающая функция
    print('Hello', name)


say_hello('Denis')
say_hello('Max')
say_hello('Anton')


def lottery():  # возвращающая функция
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    win = random.choice(tickets)
    return win


win = lottery()
print(win)


def lottery(mon, thue):  # принимающая и возвращающая функция
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon, thue)
    return win1, win2


win1, win2 = lottery('mon', 'thue')
print(win1, win2)
"""
Если мы не знаем сколько параметров будет принимать функция, 
мы можем написать, например, «*args» для обычных параметров 
и «**kwargs» для именованных.
"""


def lottery(*args, **kwargs):  # принимающая и возвращающая функция
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(*args)
    return win1, win2


win1, win2 = lottery(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print(win1, win2)


def test(a=2, b=True):
    print(a, b)


test()
test(False, 'ok')
test([1,2])
test(*[1,2])