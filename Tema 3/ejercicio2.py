peso = input('Ingresa tu peso en Kg.: ')
altura = input('Ingresa tu estatura en metros: ')

iMC = round(float(peso)/float(altura)**2, 2)

print(f'Tu índice de masa corporal es: {iMC}')
