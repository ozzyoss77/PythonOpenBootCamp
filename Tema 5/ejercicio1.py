import math

#Cáculo de un triángulo

areaTri = lambda alturaTri, baseTri: print((alturaTri * baseTri) / 2)

areaCir = lambda radioCir: print(math.pi * radioCir**2)

areaTri(alturaTri = int(input('Dime la altura del triángulo: ')), baseTri = int(input('Dime la base del triángulo: ')) )
areaCir(radioCir=int(input('Dime el radio del circulo: ')))