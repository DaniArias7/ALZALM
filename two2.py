def decimal_a_hexadecimal(decimal):
    hex_map = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    if decimal < 10:
        return str(decimal)
    elif decimal in hex_map:
        return hex_map[decimal]
    else:
        cociente = decimal // 16
        residuo = decimal % 16
        return decimal_a_hexadecimal(cociente) + decimal_a_hexadecimal(residuo)

numero_decimal = 71092
print("El número decimal", numero_decimal, "en hexadecimal es:", decimal_a_hexadecimal(numero_decimal))
