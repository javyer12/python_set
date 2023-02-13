import utils
data = [
  {
    'country': "Col",
    'population': 345
  },
   {
    'country': "arg",
    'population': 445
  },
   {
    'country': "hnd",
    'population': 35
  },
   {
    'country': "mx",
    'population': 545
  }
]
def run():
  
  keys, values = utils.get_population()
  print(keys)
  print(values)

  country = input('Insert a country: ')
  rta= utils.population_by_country(data,country)
  print(rta)


if __name__== '__main__':
  run()