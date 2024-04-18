# a = 1
# # a = str(a)
# b = "hello"
# print(str(a) + b)


# name = "Vasya"
# age = 22
# s = 123_123_123
# print(s)
# print("Привет я", name, "мне", age, "года" )
# print("Привет я " + name + " мне "+ str(age) + "года" )
# print("Привет я %s мне %d года" % (name, age))
# print("Привет я {} мне {} года".format(name, age))
# print("Привет я {1} мне {0} года".format(age, name))
# print("Привет я {name1} мне {age1} года".format(name1=name, age1=age))
# print(f"Привет я {name} мне {age} года")
# print(f"Привет я {name:*<15} мне {age} года")
# print(f"Привет я {name:=^15} мне {age} года")
# b = 12345678
# print(f"Сумма - {b:,}")
# print(f"Сумма - {b:_}")
# print(f"Сумма - {12.12162876:.3f}")
# print(f"Сумма - {323123:010}")
# print("{}:{:02}:{:02}".format(12, 1, 2)) # время

# print(len(name))

# СРЕЗЫ
# a='0123456789'
# print(a[5])
# print(a[-4])
# print(a[0:7])
# print(a[:7])
# print(a[:])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])

# a = "hello, Python - это КРУТО "
# f = a.find(" ")
# print(f)
# print(a.count('l', 0, a.find(" ")) )
# print(a.count('l', 0, f) )
# b = a.lower()
# print(a)
# a = input('sas').lower()
# a.upper()
# print(a.lower().find("круто"))

# print(a.capitalize())
# print(a.center(50,'*'))
# print(a.ljust(50,'*'))
# print(a.rjust(50,'*'))

# a = a.strip('0')
# print(a + "===")
# b = a.encode()
# print(b)
# print(b.decode())

# a = input("x4")
# a = "1 42 61 3"
# b = a.split()
# c = sum(map(int, b))
# print(c)
# c = " <-> ".join(b)
# print(b)
# print(c)

# a = "12311"
# print(a.isalpha())
# print(a.isalnum())
# print(a.isdigit())
# print(a.isnumeric())

# print(f'qq\nww\n{12345678:_}'.replace("_", " ").replace("\n", ""))
# print(a.zfill(15))

# a = "hello python"
# b = "hello"
# print(a==b)
# print(a!=b)
# print(a*10)
# print(b in a)


# b[2] = 'a' # ошибка - нельзя менять симмвол в строке по индексу

# text = "Hello---WoWoWorld---Python"
# print(text.rfind("Wo"))
# print(text.index("Wo1"))
# print(text.rindex("Wo1"))
# words2 = text.rsplit(sep="---", maxsplit=1) # сплит справа и только 1 раз
# print(words2)
# print(text.islower())
# print(text.isupper())
# print(text.istitle())
# print(text.isalpha())
# print(text.isdigit())
# print(text.isdecimal())
# print(text.isnumeric())
# print(text.isalnum())
# print(text.isspace())
# print(text.isascii())
# print(text.isidentifier())
# print(text.isprintable())
# text = "Hello python python world"
# print(text.partition("Python"))
# print(text.rpartition("Python"))

# text = "Hello world"
# print(text.endswith("rld"))
# print(text.startswith("Hel", 1, 7))

# text = "Hello world"
# print(text.removeprefix("Hell"))
# print(text.removesuffix("rld"))

# множественная замена подстрок
a = "Однажды, в студеную зимнюю пору"
b = a.maketrans({"а":"А","у":"У","и":"И"})
b = a.translate(b)
print(b)