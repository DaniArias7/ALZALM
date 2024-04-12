# 0(1)

def calcular_coeficientes(a0, a1): ##0(1)
    c1 = (6 * a1 - a0) / (6 - 1) #0(1)
    c2 = (a0 - 6 * a1) / (6 - 1) #0(1)
    return c1, c2 #0(1)

def calcular_an(n, c1, c2): ##0(1)
    if n == 0: #0(1)
        return c1 #0(1)
    elif n == 1: #0(1)
        return c1 * 6 + c2 #0(1)
    else:
        return (7/12 * 6**n) + (7/30 * (-1)**n) #0(1)

# Datos de entrada
a0 = 6  # Número de letras del primer nombre
a1 = 6  # Número de letras del primer apellido

# Calcular coeficientes
c1, c2 = calcular_coeficientes(a0, a1) #0(1)

# Imprimir coeficientes
print("Coeficiente c1:", c1) #0(1)
print("Coeficiente c2:", c2) #0(1)

# Calcular a_n para diferentes valores de n y mostrar los resultados
for n in range(10): #0(1)
    print("a_{}:".format(n), calcular_an(n, c1, c2)) #0(1)
