# conocer el path del sistema en el cual se esta trabajando
import sys 
# print(sys.path)


# modulo de expresiones regulares
import re
text = 'my numBer is 221 111 222, the country code is 504'

rta = re.findall('[A-Z]+',text)
print(rta)

# formato de fechas
import time
timestamp = time.time()
local = time.localtime()
#marca la hora del servidor donde esta corriendo python
result = time.asctime(local)
print(timestamp)
print(local)
print(result)

# frecuencia de los numeros en una lista
import collections

num = [1,2,6,85,22,22,11,1,3,5,5,7,0,22,11,4,88,32,25,5,3,23,23]

counter= collections.Counter(num)
print(counter)