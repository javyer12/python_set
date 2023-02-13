def my_print(text):
  print(text)

my_print("hola")

# funciones con return

# def func(initial_num, range_num):
#   sum = 0 
#   for num in range(initial_num,range_num):
#     sum += num 
#     print(sum)
#   return sum

# print(func(2,14))

# functions: parameter by defaults
def find_volume(lenght=2, width=2, depth=2):
  return lenght * width * depth

result = find_volume(depth = 15)
print(result)