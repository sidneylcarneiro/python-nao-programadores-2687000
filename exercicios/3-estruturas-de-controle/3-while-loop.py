# Crie duas variáveis do tipo numérica, uma sinalizando a fase atual do curso e outra o nível final
nivel_atual = 1
nivel_final = 10


# Crie um while loop que imprima na tela o nível atual
while nivel_atual <= nivel_final:
  print("seu nível é: ", nivel_atual)

  while True:
    nivel_str = input("insira um nivel de um até 4: ")
    if nivel_str.isdigit():
      nivel_atual = int(nivel_str)
      break
    else:
      print("Valor inválido. Digite um número entre 1 e 4.")

  if nivel_atual < 1:
    print("seu nível começa no 1")
  elif nivel_atual > 4:
    print("Parabéns curso concluído!")

# Insira "else" no while loop anterior.
