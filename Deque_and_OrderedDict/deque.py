from collections import deque
# append (добавить элемент в конец дека);
#appendleft (добавить элемент в начало дека);
#pop (удалить и вернуть элемент из конца дека);
#popleft (удалить и вернуть элемент из начала дека).

clients = deque()
clients.append('Ivanov')
clients.append('Petrov')
clients.append('Smirnov')
clients.append('Tikhonova')
print(clients)
# deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])

print(clients[2]) # поддерживает индексацию по элементам
# Smirnov

first_client = clients.popleft() # забрать из начала очереди pop.left()
second_client = clients.popleft()
 
print("First client:", first_client) # Функции pop и popleft возвращают тот элемент, который они удаляют
print("Second client:", second_client)
print(clients)
# First client: Ivanov
# Second client: Petrov
# deque(['Smirnov', 'Tikhonova'])

clients.appendleft('Vip-client') # добавить в начало очереди 
 
print(clients)
# deque(['Vip-client', 'Smirnov', 'Tikhonova'])

tired_client = clients.pop() # удалить последний элемент в очереди 
print(tired_client, "left the queue")
print(clients)
# Tikhonova left the queue
# deque(['Vip-client', 'Smirnov'])

clients = deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova']) # чтобы удалить элемент по индексу, пользуемся функц. ''del''
print(clients)
# deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])
del clients[2]
print(clients)
# deque(['Ivanov', 'Petrov', 'Tikhonova'])


.extend # добавить в конец дека
.extendleft # добавить в начало дека 

# В скобках передаём список при создании deque,
# чтобы сразу добавить все его элементы в очередь
shop = deque([1, 2, 3, 4, 5])
print(shop)
# deque([1, 2, 3, 4, 5])
shop.extend([11, 12, 13, 14, 15, 16, 17])
print(shop)
# deque([1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 17])


shop = deque([1, 2, 3, 4, 5])
print(shop)
# deque([1, 2, 3, 4, 5])
shop.extendleft([11, 12, 13, 14, 15, 16, 17])
print(shop)
# deque([17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5])


limited = deque(maxlen=3) # очередь с ограниченной длиной
print(limited)
# deque([], maxlen=3)
 
limited_from_list = deque([1,3,4,5,6,7], maxlen=3)
print(limited_from_list)
# deque([5, 6, 7], maxlen=3)

 # в очереди с ограниченной длиной сохраняются только последние элементы, а первые исчезают из памяти
limited.extend([1,2,3])
print(limited)
# deque([1, 2, 3], maxlen=3)
 
print(limited.append(8)) 
# None
print(limited) # limited.append(8), удаляемый элемент не возвращается, а просто исчезает
# deque([2, 3, 8], maxlen=3) 

--------------------------------------------------------------
temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]

days = deque(maxlen=7)
 
for temp in temps:
    # Добавляем температуру в очередь
    days.append(temp)
    # Если длина очереди оказалась равной максимальной длине очереди (7),
    # печатаем среднюю температуру за последние 7 дней
    if len(days) == days.maxlen:
        print(round(sum(days) / len(days), 2), end='; ')
# Напечатаем пустую строку, чтобы завершить действие параметра
# end. Иначе следующая строка окажется напечатанной на предыдущей
print("")
# Результат:
# 20.77; 21.27; 22.16; 23.3; 24.44; 24.94; 25.56; 26.2; 25.97;
# 25.94; 25.57; 25.1; 24.81; 24.21; 23.23; 22.57; 21.41; 20.4;
# 19.6; 19.1; 19.04; 18.96; 19.44; 20.01; 20.67;

--------------------------------------
dq = deque([1,2,3,4,5])
print(dq)
# deque([1, 2, 3, 4, 5])
 
dq.reverse() # reverse позволяет поменять порядок элементов в очереди на обратный 
print(dq)
# deque([5, 4, 3, 2, 1])
-------------------------------------------
dq = deque([1,2,3,4,5])
print(dq)
# deque([1, 2, 3, 4, 5])
 
dq.rotate(2) # rotate переносит n заданных элементов из конца очереди в начало
print(dq)
# deque([4, 5, 1, 2, 3])
---------------------------------------------
dq = deque([1,2,3,4,5])
print(dq)
# deque([1, 2, 3, 4, 5])
 
# Отрицательное значение аргумента переносит
# n элементов из начала в конец
dq.rotate(-2)
print(dq)
# deque([3, 4, 5, 1, 2])

------------------------------------------

dq = [1,2,4,2,3,1,5,4,4,4,4,4,3] 
print(dq.index(4)) #  index позволяет найти первый индекс искомого элемента
# 2
print(dq.count(4)) #  count позволяет подсчитать, сколько раз элемент встретился в очереди
# 6
-------------------------------------------
dq = deque([1,2,4,2,3,1,5,4,4,4,4,4,3]) # clear позволяет очистить очередь
print(dq)
# deque([1, 2, 4, 2, 3, 1, 5, 4, 4, 4, 4, 4, 3])
dq.clear()
print(dq)
# deque([])

