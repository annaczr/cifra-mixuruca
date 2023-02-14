def cifrarLetra (chave, letra):
  #variáveis e pá
  alfabeto = 'abcdefghijklmnopqrstuvwxyz'
  indice = alfabeto.index(letra)

  #decisão meio mixuruca
  if(indice + chave >= len(alfabeto)):
    novaChave = (indice + chave) - len(alfabeto)
    print(novaChave)
    letracifrada = alfabeto[novaChave]

  else:
    letracifrada = alfabeto[indice + chave]

  return letracifrada


print(cifrarLetra(6,'t'))

# def cifrarPalavra (chave, palavra):


