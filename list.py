# numbers = []
# for e in range(1,11):
#   numbers.append(e)

# print(numbers)

# # list comprehension
# number_v2 = [e * 2 for e in range(1,11)]
# print(number_v2)

# numbers = [35, 16,34,22,11,68,99, 10, 34, 37, 25]

# even_numbers = []
# for number in numbers:
#   if number % 2 == 0:
#     even_numbers.append(number)
# print('v1 =>', even_numbers)

# # Ahora usando List Comprehension 👇
# even_numbers_v2 = [number for number in numbers if number % 2 == 0]

# print('v2 =>', even_numbers_v2)



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    ls = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) ]
    print(ls)


print(range(x + 1))