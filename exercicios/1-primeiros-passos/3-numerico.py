data_nascimento = "05-10-1976"
idade_numerica = 46
altura = 1.74

# Descubra o tipo de dado de cada variável acima
print("Tipo de dados 'data_nascimento'",type(data_nascimento),"Valor",data_nascimento)
print("Tipo de dados 'idade_numerica'",type(idade_numerica),"Valor",idade_numerica)
print("Tipo de dados 'altura'",type(altura),"Valor",altura)
# Realize uma operação entre dados do tipo inteiro e float
print("multiplica idade pela altura:", idade_numerica*altura)
# Realize uma operação entre dados do tipo string e inteiro
texto=" texto "
print("repetição ou 'multiplicação' de strings:", texto*3)
print("concatenação ou 'soma' de strings:", texto+texto)

ano_nascimento = data_nascimento[6:10]
qual_a_idade = 2024 - int(ano_nascimento)
print("Ano de Nascimento:", ano_nascimento)
print("idade:", qual_a_idade)