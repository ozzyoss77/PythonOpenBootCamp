# Cálculo del año bisiesto
# Si un año es divisible entre cuatro sin residuo es un año bisiesto

def calBisiesto(numero):
    if numero % 4 == 0:
        print(f'El año {numero} es un año bisiesto, le atinaste!')
    else:
        print(f'El año {numero} no es un año bisiesto, sigue intentando.')

calBisiesto(numero=int(input('Ingresa un año para saber si es bisiesto o no: ')))