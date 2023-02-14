def cifrarLetra (chave, letra):
  # variáveis e pá
  letrasAlfabeto = 'abcdefghijklmnopqrstuvwxyz'
  indice = letrasAlfabeto.index(letra)

  #decisão meio mixuruca
  if(indice + chave >= len(letrasAlfabeto)):
    novaChave = (indice + chave) - len(letrasAlfabeto)
    print(novaChave)
    letracifrada = letrasAlfabeto[novaChave]

  else:
    letracifrada = letrasAlfabeto[indice + chave]

  return letracifrada


print(cifrarLetra(6,'t'))

# def cifrarPalavra (chave, palavra):


