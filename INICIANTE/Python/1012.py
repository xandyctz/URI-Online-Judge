# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
A,B,C = input('').split(' ')
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

TRIANGULO = (A*C)/2
CIRCULO = pi*C*C
TRAPEZIO = (A+B)*C/2
QUADRADO = B*B
RETANGULO = A*B

print('TRIANGULO: %.3f' %TRIANGULO)
print('CIRCULO: %.3f' %CIRCULO)
print('TRAPEZIO: %.3f' %TRAPEZIO)
print('QUADRADO: %.3f' %QUADRADO)
print('RETANGULO: %.3f' %RETANGULO)