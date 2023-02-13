try:
  assert 1 != 1
except AssertionError as error:
  print(error)

print("next code")

try:
  age = int(input("insert your age: "))
  if age > 18:
    print("welcome")
  else:
    raise Exception("No younger allowed")
except Exception as err:
  print(err)


print("hola")
def sam(a,b):
  return a + b

print(sam(5,7))