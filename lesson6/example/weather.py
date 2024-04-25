from pyowm import OWM


owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()


observation = mgr.weather_at_place('Grodno')


# from pprint import pprint
# print(dir(observation))
# d = observation.to_dict()
# pprint(d)

w = observation.weather
print(w.temperature('celsius')['temp'])
print(w.wind())