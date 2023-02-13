# def fan(x):
#   return x + x
# def hof(x,func):
#   return x + func(x)

# result = hof(3,fan)
# print(result)

def walk(x):
  return f"walk: {x} km per day"

def living(x, action):
  return action(x)

rta = living( 5, walk)
print(rta)

res = lambda x : print(x)
res("hola")