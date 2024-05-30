import requests

#запросы в API
year = 2023
url = f'https://api.nbrb.by/exrates/rates?ondate={year}-01-11&periodicity=0'
data = requests.get(url)
# print(dir(data))
json = data.json()

print(json)
print(json[1])

usd = list(filter(lambda cur: cur['Cur_Abbreviation']=="USD", json))[0]
print('usd-dict', usd)
print('usd -', usd['Cur_OfficialRate'])