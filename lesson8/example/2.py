
# try:

# a = 1
# b = 1
# while b != 111:
#     b = int(input("b:"))
#     if b == 0:
#         print("Ошибка")
#     else:
#         print(123*1+12*b/b)
#    
# while b != 'stop':
#     b = input("Число: ")
#     try:
#         print(100/int(b))
#     except ValueError:
#         print("Это не число")
#     except ZeroDivisionError:
#         print("на ноль делить нельзя")
#     except:
#         print("Ошибка")
#     else: # если нет ошибок
#         print("Все хорошо")
#     finally: # выполняется всегда
#         print("Я все проверил")



# a = {1:11, 2:22}
# print(a[3])

try:
    raise ValueError ("Это моя ошибка")
except:
    print("Перехватили ошибку")