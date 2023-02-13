# nameError = variable que no existe
# dividir en 0 = ZeroDivisionError
# AssertionError = tipo de error proveniente de assert (verificador)

# raise = lanzar un error

age = int(input("insert your age: "))

if age < 18:
  raise Exception("No younger allowed")
else:
  print("welcome")

# una vez lanzado el error, el resto del codigo no se ejecutara