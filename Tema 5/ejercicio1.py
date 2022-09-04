import math

#Cáculo de un triángulo

areaTri = lambda alturaTri, baseTri: print(round((alturaTri * baseTri) / 2, 2))

areaCir = lambda radioCir: print(round(math.pi * radioCir**2, 2))

areaTri(alturaTri = float(input('Dime la altura del triángulo: ')), baseTri = float(input('Dime la base del triángulo: ')) )
areaCir(radioCir=float(input('Dime el radio del circulo: ')))