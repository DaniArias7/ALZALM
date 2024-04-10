#O(log n)

def decimal_a_hexadecimal(decimal): # 0(1)
    hex_map = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    if decimal < 10: # 0(1)
        return str(decimal) # 0(1)
    elif decimal in hex_map: # 0(1)
        return hex_map[decimal] # 0(1)
    else: 
        cociente = decimal // 16 # 0(1)
        residuo = decimal % 16 # 0(1)
        return decimal_a_hexadecimal(cociente) + decimal_a_hexadecimal(residuo) #O(log n)

numero_decimal = 71092
print("El número decimal", numero_decimal, "en hexadecimal es:", decimal_a_hexadecimal(numero_decimal)) #O(log n)
