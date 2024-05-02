from pyowm import OWM
import pyowm


owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()



try:
    observation = mgr.weather_at_place('Grodno1')
except pyowm.commons.exceptions.NotFoundError:
    print('Нет такого города')
except:
    print("Что-то пошло не так")


# from pprint import pprint
# print(dir(observation))
# d = observation.to_dict()
# pprint(d)
else:
    w = observation.weather
    print(w.temperature('celsius')['temp'])
    print(w.wind())