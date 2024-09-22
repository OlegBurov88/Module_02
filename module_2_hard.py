def password(n):
    code = ''
    for i in range(1, n):
        for j in range(i, n):
            if n % (i + j) == 0 and i != j:
                code += str(i) + str(j)
    return code


n = int(input('Введите число от 3 до 20: '))
if 2 < n < 21:
    code = password(n)
    print(f'Пароль для чисела {n}: {code}')
else:
    print('WASTED')