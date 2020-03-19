# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

A,B,C = input().split(' ')
D,E,F = input().split(' ')

A = int(A)
B = int(B)
C = float(C)
D = int(D)
E = int(E)
F = float(F)

valor = (C*B)+(F*E)

print('VALOR A PAGAR: R$ %.2f' %valor)