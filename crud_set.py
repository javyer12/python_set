set_countries = {'col', 'mex','bol'}
# sabe la longitud del set
size = len(set_countries)

# ver un item en el set
print('hn' in set_countries)
print('col' in set_countries)

# agregar al set
# no se puede agregar valores repetidos (con add solo se puede agregar un valor)
set_countries.add('hn')
print(set_countries)

# actualizar (agregar un subconjunto)
set_countries.update({'ar', 'brz', 'chile'})
print(set_countries)

# eliminar
set_countries.remove('chile')
print(set_countries)

set_countries.discard('ar')
print(set_countries)

set_countries.add('arg')
print(set_countries)

set_countries.clear()
print(set_countries)