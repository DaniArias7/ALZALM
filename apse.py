import itertools

cifras_impares = [1, 3, 5, 7, 9]

combinaciones = itertools.permutations(cifras_impares, 5)

total_combinaciones = sum(1 for _ in combinaciones)

print("El número total de números de cinco cifras distintas con las cifras impares es:", total_combinaciones)
