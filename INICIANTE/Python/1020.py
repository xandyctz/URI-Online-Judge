def converter():
  idade = int(input())
  #anos
  idadeAnos = idade//365
  resto = idade % 365
  #mes
  idadeMes = resto // 30
  resto %= 30

  #dias
  idadeDias = resto // 1
  

  print('{ano:.0f} ano(s)'.format(ano=idadeAnos))
  print('{mes:.0f} mes(es)'.format(mes=idadeMes))
  print('{mes:.0f} dia(s)'.format(mes=idadeDias))

if __name__ == '__main__':
  converter()