from math import sqrt

def eixos():
  x1,y1 = input().split()
  x2,y2 = input().split()

  x1 = float(x1)
  y1 = float(y1)
  x2 = float(x2)
  y2 = float(y2)

  line1 = x2-x1
  line2 = y2-y1
  soma = (line1*line1)+(line2*line2)
  res = sqrt(soma)
  print('%.4f' %res)
eixos()