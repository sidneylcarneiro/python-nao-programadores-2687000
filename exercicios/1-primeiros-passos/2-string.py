resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela a variável "resumo"
#print(resumo)
print("resumo:", resumo)
# Imprima na tela apenas a segunda letra da variável
segletra = resumo[1]
print("segunda letra:", segletra)
# Imprima na tela Nome
nome = resumo[0:6]  
print("Nome:", nome)
# Imprima na tela a idade de Paloma (resposta esperada: "46")
idade = resumo[23:25]  
print("Idade", idade)
# Imprima na tela o trecho final da variável
final = resumo[31:]  
print("Parte Final: ", final)

# Converta todos as letras para minúsculo e imprima na tela
print("Caixa Baixa:", resumo.lower())

# Converta todas as letras para maiúscula e imprima na tela
print("Caixa Alta:", resumo.upper())

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela
print("Título:", resumo.title())

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela
print("Capitular:", resumo.capitalize())

# Imprima na tela uma string utilizando uma variável, usando o recurso string format
print("'string format':",f"Paloma é uma mulher de {idade} anos que deseja mudar de profissão, por isso está estudando 'python'.")

###############  Outros exemplos  ####################

my_string = "Hello, world!"
print("my_string", my_string)
# Access the first character
first_char = my_string[0]  # This will be 'H'
print("first_char", first_char)
# Access a substring from index 7 (inclusive) to 12 (exclusive)
substring = my_string[7:12]  # This will be 'world'
print("substring", substring)