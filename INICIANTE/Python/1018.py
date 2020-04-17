def main():
  valor = int(input())
  troco = valor

  cem = troco//100
  troco = troco - (cem*100)

  ciquenta = troco//50
  troco = troco - (ciquenta*50)

  vinte = troco//20
  troco = troco - (vinte*20)

  dez = troco//10
  troco = troco - (dez*10)

  cinco = troco//5
  troco = troco - (cinco*5)

  dois = troco//2
  troco = troco - (dois*2)

  print(valor)
  print('%i nota(s) de R$ 100,00' %cem)
  print('%i nota(s) de R$ 50,00' %ciquenta)
  print('%i nota(s) de R$ 20,00' %vinte)
  print('%i nota(s) de R$ 10,00' %dez)
  print('%i nota(s) de R$ 5,00' %cinco)
  print('%i nota(s) de R$ 2,00' %dois)
  print('%i nota(s) de R$ 1,00' %troco)

if __name__ == '__main__':
  main()