'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''

def factorial2(n):
   if n == 0:
       return 1
   return factorial2(n - 1) * n

print(factorial2(5))