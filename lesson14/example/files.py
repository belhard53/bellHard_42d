# режимы
# w - перезапись
# r - чтение
# a - запись с добавлением

# class File:
    # def __init__(self, name):
    #     self.name = name
    
    # # для открытия через with
    # def __enter__(self):
    #     self.f = open(self.name)
    #     return self.f
    
    # # выполняется когда закончится отступ в with
    # def __exit__(self):
    #     self.f.close()
    
    

# f = open(f'lesson14\\111.txt', 'w', encoding='utf8')
# f.write('Hello Python\n')
# f.write('Hello Python\n')
# f.write('Привет Пайтон\n')
# f.close()



# with open('lesson14\\111.txt', 'r', encoding='utf8') as f:
#     for line in f:
#         print(line, end='')    

# with open('lesson14\\222.txt', 'r', encoding='utf8') as f:
#     lines = f.readlines()
#     data = lines[2].split()[2]
#     print(lines)
#     print(data)
    
#pandas
# d = {1:11, 2:22, 3:33}

import json
# with open('lesson14\\111.json', 'w') as f:
#     json.dump(d, f)

with open('lesson14\\111.json', 'r') as f:    
    d = json.load(f)
    
print(d, type(d))

# сохранить любой объект
import pickle
with open('lesson14\\111.dat', 'wb') as f:    
    pickle.dump(d, f)
    
with open('lesson14\\111.dat', 'rb') as f:    
    d = pickle.load(f)    

    print(d)




# print(data)
