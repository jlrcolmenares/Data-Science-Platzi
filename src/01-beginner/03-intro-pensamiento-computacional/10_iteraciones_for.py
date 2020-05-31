corona_cases = {
    'Spain': 1700,
    'Italy': 24000,
    'France': 800,
}
#print(corona_cases, type(corona_cases))
#print(iter(corona_cases)) comprobar que es una variable iterable

#comprobar función next()
# iterator = iter(corona_cases)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) #Error StopIteration

for pais in corona_cases.keys():
    print(pais)

for casos in corona_cases.values():
    print(pais)

for pais, casos in corona_cases.items():
    print(pais, casos)
    