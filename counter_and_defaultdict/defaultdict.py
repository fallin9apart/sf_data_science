from collections import defaultdict
groups = defaultdict(list)


students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]


for student, group in students:
    groups[group].append(student)

print(groups)

print(groups[3]) # Получить элемент из defaultdict по ключу можно так же, как и из обычного словаря

print(groups[2021]) # Если запрашиваемого ключа нет в словаре, KeyError не возникнет. Вместо этого будет напечатан пустой элемент, который создаётся в словаре по умолчанию

