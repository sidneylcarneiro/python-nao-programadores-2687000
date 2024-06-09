# Crie uma lista apenas com elementos numéricos
lista1 = [255, 255, 255, 0]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista2 = [255, "nome", [255,255,255,0], lista1, True, 2000]
# Imprima na tela apenas os 5 primeiros elementos da lista
print("Lista 2:",lista2)
primeiros_5_itens = lista2[:5]  # Fatiamento da lista para obter os 5 primeiros itens
print("Primeiros 5 itens:",primeiros_5_itens)
# Crie um slice na lista para que imprima na tela os elementos de índice par
print("Elementos Pares:",lista2[0:-1:2])
# Remova da lista o último item
print("Último item da Lista 2:",lista2[-1])
if lista2[-1] == 2000 :
  lista2.pop()
else :
  lista3 = [2000]
  lista2.extend(lista3)

print("Removido último item da Lista 2:",lista2)
print("Nova Lista 2:",lista2)
print("Último item da Lista 2:",lista2[-1])

# Insira na lista um novo item
lista3 = [2000]
print("Insira na lista um novo item:",lista3)
lista2.extend(lista3)
print("Último item da Lista 2:",lista2[-1])
print("Nova Lista 2:",lista2)

# Remova da lista um item específico
print("Remova da lista um item específico '2000'")
lista2.remove(2000)
print("Nova Lista 2:",lista2)
