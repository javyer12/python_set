# nunca se puede obtener un array mayor a la longitud del array original
# es inmutable
number = [1,2,3,4,5]
new = list(filter(lambda x:x /2 != 1, number))

print(number)
print(new)