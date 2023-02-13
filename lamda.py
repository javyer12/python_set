# reconocer los parametros de entrada y salida
# x = parametro de entrada
# x+1 = datos de salida

lam = lambda x : x + 1
print(lam(4))

hello = lambda text : print(text)
hello("hola")

# funcion que encuentra el valor de x, se le pasa un parametro cuyo valor sera la raiz cuadrada de x
def squared(valor):
  result = valor * valor
  x = result
  print(f"correct: {x}")

  
squared(53)
