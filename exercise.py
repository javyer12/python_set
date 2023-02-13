countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

print(countries)
new_set = set()
# Escribe tu solución 👇
new_set = countries.union(northAm, southAm, centralAm)
print(new_set)