'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''

a = "asasassdb"

b = {c:a.count(c) for c in set(a)}

print(dict(sorted(b.items(), key=lambda x:x[1], reverse=True)))