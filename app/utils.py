def get_population():
  keys = ['col','bol']
  values = [200,100]
  return keys,values

def population_by_country(data,country):
  result = list(filter(lambda item:item['country'] == country, data))
  return result