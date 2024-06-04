import pandas as pd

a = pd.read_csv('lesson15\\example\\auto.csv', sep = ";", names=["name", "model", "year1", "year2"])


# print(a)
# #
# # l = a['name'].unique()
# l = a.nunique() # количество уникальных во всех столбцах
# print(l)


# print(a[a['name'] == 'BMW'])
# print(a[a.name == 'Opel'])
# print(a.loc[a['name'] == 'Acura'])
# print(a.loc[a['name'].isin(['Mazda', 'BMW', 'Opel'])])
# print(a.loc[(a['name'] == 'Acura') & (a['model'] == "CL")])
# print(111,a.iloc[:3])
#
# print(a[['name']].count())
# print(a.set_index('name').filter(like='cura', axis=0) # regex='^cura'

print(a[a['name'].str.contains("ia")]) # фильтр как Like

# print(a)

# print(a.filter(like='m', axis=1))


# print('____')
# print(a.year1.min())
# print(a.mean())
# print(a.name.min())

# print(a.groupby('name').sum()) # выводит столбйы только с цифрами
# print(a.groupby('name').min()[['year1']])
# print(a.groupby('name').min().year1)


# root.mainloop()