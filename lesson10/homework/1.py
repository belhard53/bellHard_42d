"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    res = {}
    if all([type(i) is int for i in args]):
        res['args_sum'] = sum(args)
    else:
        raise TypeError("Все позиционные аргументы должны быть целыми")

    if all([type(i) is str for i in kwargs.values()]):
        res['kwargs_max_len'] = max([len(i) for i in kwargs.values()])
    else:
        raise TypeError("Все аргументы - ключевыеслова должны быть строками")

    return res

try:    
    print(dict_from_args(1, 2, "3", 4, 5,  t='ee', q='123', w='19', e='12', r='qwerty'))
except Exception as e:
    print(e)
