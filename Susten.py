SEGÚN ESTOS CODIGOS CAMBIA LO QUE YO TE DIGA PARA CADA UNO.

PARA EL CODIGO 3 

CODIGO 1

# 1. Encontrar la posición n=100

# Encuentre una relación de recurrencia, con una condición inicial, que determine de manera única cada una de las siguientes progresiones geométricas

# B) 6, -18, 54, -162,...

#----------------NO RECURSIVO-------------------

def termino_n_geometrica(a1, r, n):
    if not all(isinstance(arg, (int, float)) for arg in (a1, r, n)) or n <= 0:
        raise ValueError("Los argumentos deben ser: a1 (número), r (número), y n (entero positivo).")
    if r == 0 and n > 1:
        raise ValueError("r no puede ser cero si n es mayor que 1.")
    return a1 * (r ** (n - 1))

try:
    a1 = 6
    r = -3
    n = 100

    termino_100 = termino_n_geometrica(a1, r, n)
    print("El término en la posición n=100 es:", termino_100)
except ValueError as e:
    print("Error:", e)


#-----------------RECURSIVO---------------------

def term_n(a1, r, n):
    if not isinstance(a1, (int, float)) or not isinstance(r, (int, float)) or n <= 0:
        raise ValueError("Los parámetros a1 y r deben ser números enteros o flotantes, y n debe ser un entero positivo.")
        
    if n == 1:
        return a1
    else:
        return r * term_n(a1, r, n-1)

try:
    a1 = 6
    r = -3
    n = 100
    a_100 = term_n(a1, r, n)
    print("El término en la posición n=100 es:", a_100)
except ValueError as e:
    print("Error:", e)


CODIGO 2:

# NO-RECURSIVO---------------------------------------------------
def resolver_recurrencia(coeficientes, condiciones_iniciales, n):
    # Verificar si la recurrencia es lineal homogénea
    grado = len(coeficientes) - 1
    if grado < 0:
        return 0  # Recurrencia trivial f(n) = 0

    # Verificar si hay suficientes condiciones iniciales
    if len(condiciones_iniciales) <= grado:
        raise ValueError("No hay suficientes condiciones iniciales para resolver la recurrencia.")

    # Crear una lista para almacenar los términos de la secuencia
    secuencia = condiciones_iniciales[:]

    # Calcular los términos adicionales de la secuencia hasta alcanzar n
    for i in range(len(secuencia), n + 1):
        nuevo_termino = 0
        for j in range(1, grado + 1):
            nuevo_termino += coeficientes[j] * secuencia[i - j]
        secuencia.append(nuevo_termino)

    # Devolver el término n de la secuencia
    return secuencia[n]

#RECURSIVO-----------------------------------------------
def resolver_recurrencia_recursivo(coeficientes, condiciones_iniciales, n):
    # Comprueba si n está dentro del rango de condiciones iniciales
    if n < len(condiciones_iniciales):
        return condiciones_iniciales[n]

    # Inicializa la lista de la secuencia con las condiciones iniciales
    secuencia = condiciones_iniciales[:]

    # Calcula los términos adicionales de la secuencia hasta alcanzar n
    for i in range(len(condiciones_iniciales), n + 1):
        nuevo_termino = 0
        # Aquí se produce la recursión para calcular el nuevo término
        for j in range(1, len(coeficientes)):
            nuevo_termino += coeficientes[j] * secuencia[i - j]
        secuencia.append(nuevo_termino)

    # Devuelve el término n de la secuencia
    return secuencia[n]



# Coeficientes y condiciones iniciales específicos para el problema dado
coeficientes = [2, -2]  # Coeficientes de la recurrencia: a_n = 2*a_{n-1} - 2*a_{n-2}
condiciones_iniciales = [4, 1]  # Condiciones iniciales: a_0 = 4, a_1 = 1
n =  1879  # Calcular a_1000

resultado = resolver_recurrencia(coeficientes, condiciones_iniciales, n)
print("El valor de la recurrencia en el índice", n, "es:", resultado)

resultado2 = resolver_recurrencia_recursivo(coeficientes, condiciones_iniciales, n)
print("Con recursion el valor de la recurrencia en el índice", n, "es:", resultado2)

CODIGO 3:

#NORECURSIVO
def geometric_progression_term(a, r, n):
    if n <= 0:
        raise ValueError("La posición n debe ser un entero positivo.")
    term_n = a * (r ** (n - 1))
    return term_n
#RECURSIVO
def geometric_progression_term_r(a, r, n):
    if n <= 0:
        raise ValueError("La posición n debe ser un entero positivo.")
    term_n = a * (r ** (n - 1))
    return term_n
    
def find_ratio():
    r = 5 / 4
    return r

def interpolated_term(a, r, n):
    if n <= 0:
        raise ValueError("La posición n debe ser un entero positivo.")
    
    # Calcular la parte entera de n
    integer_part = int(n)
    # Calcular la parte decimal de n
    decimal_part = n - integer_part
    
    # Calcular el término en la posición n sin la parte decimal
    term_n = geometric_progression_term(a, r, integer_part)
    
    # Calcular el siguiente término
    next_term = geometric_progression_term(a, r, integer_part + 1)
    
    # Calcular el término interpolado
    interpolated_term = term_n + decimal_part * (next_term - term_n)
    
    return interpolated_term

try:

    a = 1  # Primer término
    n = 1245.123  # Posición


    r = find_ratio()


    term_n = interpolated_term(a, r, n)
    print("El término en la posición", n, "es:", term_n)

except ValueError as ve:
    print("Error:", ve)

CODIGO 4:

########### Encontrar n =151’145.018. y multiplicarlo por el número de letras de su nombre ############

###################################### No recursivo ###########################################

def calcular_termino(n):
    if not isinstance(n, int):
        raise TypeError("El valor de n debe ser un entero.")
    
    if n < 0:
        raise ValueError("El valor de n debe ser no negativo.")

    nombre_multiplicado = len("Dilan")

    # Valores iniciales multiplicados por el nombre
    a_0 = 1 * nombre_multiplicado
    a_1 = 3 * nombre_multiplicado

    if n == 0:
        return a_0
    elif n == 1:
        return a_1

    try:
        # Inicializamos una lista para almacenar los valores calculados
        a = [None] * (n + 1)
        a[0] = a_0
        a[1] = a_1

        # Hacemos un ciclo para calcular los términos sucesivos de la recurrencia iniciando desde 2
        for i in range(2, n + 1):
            a[i] = 5 * a[i - 1] + 6 * a[i - 2]

            # Si se supera el límite permitido, lanzamos una excepción
            if a[i] > 10**99999:
                raise ValueError("Error: El valor del término en la posición {} supera el límite permitido.".format(n))

            # Si el valor resultante es negativo, lanzamos una excepción
            if a[i] < 0:
                raise ValueError("Error: El valor del término en la posición {} es negativo.".format(n))

        # Retornar el término en la posición n
        return a[n]
    except IndexError as error_indice:
        raise IndexError("Error de índice durante el cálculo del término en la posición {}: {}".format(n, error_indice))
    except MemoryError as error_memoria:
        raise MemoryError("Error de memoria durante el cálculo: {}".format(error_memoria))
    except RecursionError as error_recursion:
        raise RecursionError("Error de recursión: {}".format(error_recursion))

# Calculamos el número en la posición n
n = 151145018
try:
    resultado = calcular_termino(n)
    print("El término en la posición n =", n, "es:", resultado)
except ValueError as error_valor:
    print("Error:", error_valor)
except OverflowError as error_desbordamiento:
    print("Error:", error_desbordamiento)
except TypeError as error_tipo:
    print("Error:", error_tipo)
except IndexError as error_indice:
    print("Error:", error_indice)
except MemoryError as error_memoria:
    print("Error en la capacidad de memoria usable:", error_memoria)
except RecursionError as error_recursion:
    print("Error en el calculo:", error_recursion)


#################################### Recursivo #############################################

def calcular_termino_recursivo(n):
    if not isinstance(n, int):
        raise TypeError("El valor de n debe ser un entero.")
    
    if n < 0:
        raise ValueError("El valor de n debe ser no negativo.")

    nombre_multiplicado = len("Dilan")

    if n == 0:
        return 1 * nombre_multiplicado
    elif n == 1:
        return 3 * nombre_multiplicado

    try:
        # Usamos la fórmula para calcular el término en la posición n recursivamente
        return 5 * calcular_termino_recursivo(n - 1) + 6 * calcular_termino_recursivo(n - 2)
    except RecursionError as error_recursion:
        raise RecursionError("Error de recursión: {}".format(error_recursion))
    except MemoryError as error_memoria:
        raise MemoryError("Error de memoria durante el cálculo: {}".format(error_memoria))

# Calculamos el número en la posición n
n = 151145018
try:
    resultado = calcular_termino_recursivo(n)
    print("El término en la posición n =", n, "es:", resultado)
except ValueError as error_valor:
    print("Error:", error_valor)
except RecursionError as error_recursion:
    print("Error en el cálculo:", error_recursion)
except MemoryError as error_memoria:
    print("Error en la capacidad de memoria usable:", error_memoria)
except TypeError as error_tipo:
    print("Error:", error_tipo)
