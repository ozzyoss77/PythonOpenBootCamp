# Cálculo para saber si un número es primo o no


def es_primo(numero):
    contador = 0

    for i in range(1, numero):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
        if contador >= 2:
            break

    if contador == 0:
        print(f'El {numero} es primo!!!')
    else:
        print(f'El {numero} NO es primo!!!')


es_primo(numero=int(input('Dime un numero (entero): ')))