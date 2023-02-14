def cifrarLetra (chave, letra):
  #variáveis e pá
  alfabeto = 'abcdefghijklmnopqrstuvwxyz'
  index = alfabeto.index(letra)

  #decisão meio mixuruca
  if(index + chave >= len(alfabeto)):
    novaChave = (index + chave) - len(alfabeto)
    print(novaChave)
    letracifrada = alfabeto[novaChave]

  else:
    letracifrada = alfabeto[index + chave]

  return letracifrada


print(cifrarLetra(6,'t'))

# def cifrarPalavra (chave, palavra):


