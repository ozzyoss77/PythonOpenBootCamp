# Cálculo para saber si un número es primo o no


def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1

    if contador == 0:
        print(f'El {numero} es primo!!!')
    else:
        print(f'El {numero} NO es primo!!!')


es_primo(numero=int(input('Dime un numero (entero): ')))