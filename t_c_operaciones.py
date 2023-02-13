set_a = {'col', 'hn', 'mexico', 'us'}
set_b = {'pe', 'bol', 'mexico', 'us'}

# crear una union
# set_c = set_a.union(set_b)
# print(set_c)

# miVariable = "camel case"
# mi_variable = "snake case"
# MiVariable = "pascal case"
# print(miVariable)
# print(mi_variable)
# print(MiVariable)

# unpacking
# colo,pe,mexico,hn,us,bol = set_c
# print(colo)
# print(bol)
# print(us)
# print(hn)
# print(mexico)
# print(pe)

# intercepcion
# imprime solo los valores dentro de la intercepcion (elementos en comun)
set_c =  set_a.intersection(set_b)
print(set_c)

# print(set_a & set_b)

# dierencia
# set_c = set_a.difference(set_b)
# print(set_c)
# set_d = set_b.difference(set_a)
# print(set_d)
# print(set_a - set_b)


# diferencia simetrica
set_c = set_a.symmetric_difference(set_b)
print(set_c)
# signo de intercalacion
print(set_a ^ set_b)