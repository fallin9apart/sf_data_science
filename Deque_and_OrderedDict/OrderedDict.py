from collections import OrderedDict     # Специальный словарь, который гарантирует сохранение ключей в порядке их добавления

data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
ordered_client_ages = OrderedDict(data)
print(ordered_client_ages)

ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[1])) # сортировка, объекты будут добавлены в порядке сортировки(sorted)
print(ordered_client_ages)

del ordered_client_ages['Andrey'] # Если удалить элемент, а затем добавить его снова, он также окажется в конце
print(ordered_client_ages)
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Maria', 20), ('Nikita', 18)])
ordered_client_ages['Andrey'] = 23
print(ordered_client_ages)
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Maria', 20), ('Nikita', 18), ('Andrey', 23)])

