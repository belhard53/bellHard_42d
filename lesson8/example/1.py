# a = "dsds"
# print(a)



# def get_weather(city):
#     w = f"Погода {city}"
#     w = dict(city=city, rain=True, temp=19, sunset = '19:00')    
#     return w

def print_weather(city12, rain=False):
    print(f"Погода в {city12}")
    if rain:
        print("Дождь")
    
# def print_weather(weather):
#     print(*[f'{key} - {weather[key]}' for key in weather], sep='\n')
    

    
print_weather('Grodno', True)

# cityes = ['Grodno', 'Minsk', 'Gomel']
# for city in cityes:    
#     print_weather(city)
    
# print(print_weather('dsds'))
    
    
# cityes = [('Grodno', True), ('Minsk', False), ('Gomel', False)]
# for city in cityes:    
#     print_weather(*city)
    
    
# weather_dict = get_weather('Minsk')
# print_weather(weather_dict)


# print(print("123"))
# print(type(print(123)))


# def p10(text, n=1):
#     for i in range(n):
#         print(text)
    
    
# def maxn(a, b):
#     return a if a>b else b

# print(maxn(maxn(4,2), 3))

