# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
lista = list(range(1,31))

# 2. Crie um for loop para percorrer todos os elementos da lista
# 3. Crie uma estrutura condicional para verificar cada número da lista:
indice = 0
for i in lista:
  if i % 3 == 0 and i % 5 == 0 :
    lista[indice] = "FIZZBUZZ"
    #  print(lista[indice])
  elif i % 3 == 0 :
    lista[indice] = "FIZZ"
    #  print(lista[indice])
  elif i % 5 == 0 :
    lista[indice] = "BUZZ"
    #  print(lista[indice])
  else:  
    lista[indice] = i
    # print(lista[indice])
  indice += 1

print(lista)

# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"

