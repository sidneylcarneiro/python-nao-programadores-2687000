# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:

# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
#nome = input("Qual é o seu nome? ")
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
#total_dias = input("Quantos dias por semana você costuma estudar? ")

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
#total_horas = input("Quantos horas por dia você costuma estudar? ")

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
#curso = input("Qual é o nome do seu curso? ")
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
#print(f"""Nome: {nome}
#Dias dedicados aos estudos: {total_dias}
#Horas dedicadas aos estudos: {total_horas}
#Nome do Curso: {curso}
#Horas dedicadas por semana: {int(total_dias)*int(total_horas)}""")


#Outra abordagem

while True:
    try:
        nome = input("Qual é o seu nome? ")
        if nome.isalpha() or nome.isspace():  # Verifica se é apenas letras ou espaços em branco
            break
        else:
            print("Erro: Digite apenas letras e espaços em branco para o nome: ")
    except ValueError:
        pass  # Ignora exceções de ValueError, pois não são relevantes para este caso

while True:
    try:
        total_dias = int(input("Quantos dias por semana você costuma estudar? "))
        if 1 <= total_dias <= 7:
            break
        else:
            print("Valor de dias inválido. Digite um número entre 1 e 7: ")
            #total_dias = int(input("Valor de dias inválido. Digite um número entre 1 e 7: "))
    except ValueError:
        print("Erro: Digite um número inteiro: ")
        #total_dias = int(input("Erro: Digite um número inteiro."))
while True:
    try:
        total_horas = int(input("Quantas horas por dia você costuma estudar? "))
        if 1 <= total_horas <= 23:
            break
        else:
            print("Valor de horas inválido. Digite um número entre 1 e 23: ")
    except ValueError:
        print("Erro: Digite um número inteiro: ")

while True:
    try:
        curso = input("Qual é o nome do seu curso? ")
        if curso.isalpha() or curso.isspace():  # Verifica se é apenas letras ou espaços em branco
            break
        else:
            print("Erro: Digite apenas letras e espaços em branco para o nome do curso: ")
    except ValueError:
        pass  # Ignora exceções de ValueError, pois não são relevantes para este caso

print(f"""Olá {nome}! 
      Você dedica aos estudos: {total_dias} dias, {total_horas} horas diárias.
      Portanto você dedica ao Curso {curso}: {int(total_dias)*int(total_horas)} horas por semana! """)
