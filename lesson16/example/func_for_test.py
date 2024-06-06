from math import pi


def circle_area(r):
    # isinstance(True, int) = True поэтому через type    
    if type(r) not in [int, float]:
        raise TypeError('type err')
    if r < 0:
        raise ValueError('val err')
    return pi*r**2



def sum_of_numbers(n: int, s=0):
    if s == len(str(n)): return 0
    return sum_of_numbers(n, s + 1) + int(str(n)[s])


def test_circle_area():
    #самостоятельная проверка без посторонних библиотек
    
    #проверка типов
    data = [1, 5, 8, 0, -4, True, False, 2.212, '22', 'три', [2, 2], 2+3j]
    for r in data:
        mes = 'Площадь с радиусом {} - {}'
        try:
            print(mes.format(r, circle_area(r)))
        except  Exception as e:
            print(r, "- errr", e)
            
            
    #проверка расчета
    data = [[1, 3.14], [4, 12], [100, 1000]] 
    for r, val in data:
        mes = 'Площадь с радиусом {} - {}'
        try:
            res = circle_area(r)
            assert res == val            
        except  Exception as e:
            print(r, "- errr", e)

if __name__ == '__main__':    
    
    test_circle_area()