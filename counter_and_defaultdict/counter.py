from collections import Counter

cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter(cars)
print(c)
print(c['black']) #  узнать сколько раз встретился 
print(c['purple']) # ошибка не возникнет
print(sum(c.values())) # узнать сумму всех значений в Counter


cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow'] 
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

# получим для них счетчики 
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)

print(counter_moscow + counter_spb) # можно сложить два исходных счетчика 

counter_moscow.subtract(counter_spb) # узнать разницу между объектами(вычитание)
print(counter_moscow)

print(*counter_moscow.elements()) # получить список всех элементов(в алфавитном порядке)

print(list(counter_moscow)) # получить список уникальных элементов 

print(dict(counter_moscow)) # превратить в обычный словарь

print(counter_moscow.most_common()) # получить список из кортежей элементов в порядке убывания их встречаемости
print(counter_moscow.most_common(2)) # желаемое число первых наиболее встречаемых элементов

counter_moscow.clear # обнулить счетчик 

   

