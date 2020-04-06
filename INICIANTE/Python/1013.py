# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
a,b,c = input('').split(' ')

a = int(a)
b = int(b)
c = int(c)

maiorAB = (a+b+abs(a-b))/2
maiorABC = (maiorAB+c+abs(maiorAB-c))/2

print('%i eh o maior' %maiorABC)