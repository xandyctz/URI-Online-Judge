def main():
  valor = float(input())
  valor +=0.001
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

  moedaUm = troco//1
  troco = troco - (moedaUm*1)

  moedaCiquente = troco//0.50
  troco = troco - (moedaCiquente*0.50)

  moedaVinte = troco//0.25
  troco = troco - (moedaVinte*0.25)

  moedaDez = troco//0.10
  troco = troco - (moedaDez*0.10)

  moedaCinco = troco//0.05
  troco = troco - (moedaCinco*0.05)

  moedaUmCentavo = troco//0.01
  troco = troco - (moedaUmCentavo*0.01)

  print('NOTAS:')
  print('%.0f nota(s) de R$ 100.00' %cem)
  print('%.0f nota(s) de R$ 50.00' %ciquenta)
  print('%.0f nota(s) de R$ 20.00' %vinte)
  print('%.0f nota(s) de R$ 10.00' %dez)
  print('%.0f nota(s) de R$ 5.00' %cinco)
  print('%.0f nota(s) de R$ 2.00' %dois)

  print('MOEDAS:')
  print('%.0f moeda(s) de R$ 1.00' %moedaUm)
  print('%.0f moeda(s) de R$ 0.50' %moedaCiquente)
  print('%.0f moeda(s) de R$ 0.25' %moedaVinte)
  print('%.0f moeda(s) de R$ 0.10' %moedaDez)
  print('%.0f moeda(s) de R$ 0.05' %moedaCinco)
  print('%.0f moeda(s) de R$ 0.01' %moedaUmCentavo)

if __name__ == '__main__':
  main()