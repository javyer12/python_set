set_countries = {
  'col',
  'mex',
  'bol'
}
print(set_countries)
print(type(set_countries))

# los conjuntos no pueden tener valores repetidos.
# conjunto con varios tipos de datos
set_types = {1, "hola", False}
print(set_types)

# conjunto a partir de string
set_string = set("casa")
print(set_string)

# conjunto a partir de una tupla
set_tuples = set(('abc','abc','cvc','asa'))
print(set_tuples)

# conjunto apartir de una lista
num =[10,2,8,3,4,5,6,6,7]
set_list = set(num)
print(set_list)
# pasar el conjunto de numeros unicos a una lista
num_list = list(set_list)
print(set_list)
