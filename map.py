# igual que el map de js
# podemos transformar los elementos

# rta = [1,2,3,4]
# def gun(rt):
  # convertirla a lista. porque simplemente map regresa la referencia del objeto
#   return list(map(lambda x:x *5, rt))

# res = gun(rta)
# print(res)

# map con diccionarios

items = [
  {
    "product": "camisa",
    "price": 100
  },
  {
    "product": "pantalones",
    "price": 300
  },
  {
    "product": "short",
    "price": 100
  }
]

prices = list(map(lambda item: item['price'], items))

stuck = list(map(lambda s: s['product'], items))

print(prices)
print(f"item:  {items}")

def add_tax(i):
  item = i.copy();
  item['taxes']  = round(item['price'] * .19)
  return item

new_item = list(map(add_tax, items))
print(f"new  {new_item}")

# map con inmutabilidad
 # map no crea otra lista, asi que modifica al original (ambos apuntan a la misma referencia en memoria)

