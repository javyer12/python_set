# file = open('./text.txt')
# # read lee el archivo
# # print(file.read())

# print('""""""""')
# # readline = lee el archivo linea por linea
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())


# # cerrar el archivo
# file.close()



with open('./text.txt') as file:
  for line in file:
    print(line)