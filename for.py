for i in 1, 2, 3, 4:
    print(i)
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in 'hello':
    print(i)

list_ = ['one', 'two', 'three']
for i in list_:
    print(i)

list_ = ['one', 'two', 'three']
for i in list_:
    if i == 'three':
        list_.remove(i)
print(list_)

list_ = ['one', 'two', 'three']
for i in range(len(list_)):
    print(list_[i])
    list_[i] = ' ;( '
print(list_)

sum_ = 0
list_2 = [2, 3, 4, 5, 1]
for i in range(len(list_2)):
    sum_ += list_2[i]  # аналогично sum_ = sum_ + list_2[i]
print(sum_)

for i in range(1, 11):  # range(stop){0-stop}, range(start, stop, step)
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')

dict_ = {'a': 1, 'b': 2, 'c': 3}
for i in dict_:
    print(i, dict_[i])

for i, j in dict_.items():
    print(i, j)
