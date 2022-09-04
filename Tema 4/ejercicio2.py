initialNUmber = int(input('Ingresa un número por favor: '))
finalNumber = int(input('Ingresa un número mas alto que el anterior: '))

for number in range(initialNUmber, (finalNumber + 1)):
    if number % 2 != 0:
        print(number)