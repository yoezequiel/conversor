def decimal_a_binario(decimal):
    return bin(decimal)[2:]

def decimal_a_octal(decimal):
    return oct(decimal)[2:]

def decimal_a_hexadecimal(decimal):
    return hex(decimal)[2:]

def binario_a_decimal(binario):
    return int(binario, 2)

def octal_a_decimal(octal):
    return int(octal, 8)

def hexadecimal_a_decimal(hexadecimal):
    return int(hexadecimal, 16)

def obtener_tipo_numero():
    while True:
        tipo = input("Ingresa el tipo de número \n-decimal \n-binario \n-octal \n-hexadecimal:\n")
        if tipo in ["decimal", "binario", "octal", "hexadecimal"]:
            return tipo
        else:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("Tipo de número inválido. Intenta nuevamente.")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

tipo_origen = obtener_tipo_numero()
numero = input(f"Ingrese un número {tipo_origen}: ")

if tipo_origen == "decimal":
    decimal = int(numero)
    binario = decimal_a_binario(decimal)
    octal = decimal_a_octal(decimal)
    hexadecimal = decimal_a_hexadecimal(decimal)
elif tipo_origen == "binario":
    binario = numero
    decimal = binario_a_decimal(binario)
    octal = decimal_a_octal(decimal)
    hexadecimal = decimal_a_hexadecimal(decimal)
elif tipo_origen == "octal":
    octal = numero
    decimal = octal_a_decimal(octal)
    binario = decimal_a_binario(decimal)
    hexadecimal = decimal_a_hexadecimal(decimal)
else:
    hexadecimal = numero
    decimal = hexadecimal_a_decimal(hexadecimal)
    binario = decimal_a_binario(decimal)
    octal = decimal_a_octal(decimal)
print("-----------------------")
print("Decimal:", decimal)
print("Binario:", binario)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)
