# importar reduce
import functools

numbers = [1,2,3,5,7]
result = functools.reduce(lambda counter, item: item + counter, numbers)

print(result)

