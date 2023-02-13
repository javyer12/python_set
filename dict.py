# dict = {}
# for i in range(1,11):
#   dict[i] = i *2

# print(dict)


# dic comprehension
# dict_2 = {i : i * 2 for i in range(1,5)}
# print(dict_2)
import random

# countries = ['col','mex','bol', 'pe']
# population = {}

# for country in countries:
#   population[country] = random.randint(1,100)

# print(population)

# country es la llave (aqui va la logica), luego a cada elemento que se itera se le aplcara esa logica
# population_2  = {country : random.randint(1,100) for country in countries}

# print(population_2)

# names = ['nico', 'zule', 'santi']
# ages = [12,56,98]

# print(list(zip(names, ages)))
# crea una lista de tuplas
# solo zip crea una referencia a una lista
# persons = {name : age for (name,age) in zip(names,ages)}
# print(persons)


mundiales = [1998,2002,2006,2010,2014,2018,2022]
campeones = ["Francia", "Brazil", "Italia", "España", "Alemania", "Francia", "Argentina"]

campeonas = {mundial: campeon for (mundial, campeon) in zip(mundiales,campeones)}

print(campeonas)