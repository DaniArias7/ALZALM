#O(n!)

import itertools

cifras_impares = [1, 3, 5, 7, 9] # 0(1)

combinaciones = itertools.permutations(cifras_impares, 5) # O(n!)

total_combinaciones = sum(1 for _ in combinaciones) # O(n!)

print("El número total de números de cinco cifras distintas con las cifras impares es:", total_combinaciones) # 0(1)
