# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica1 estudante = {}
# estudante['nome'] = input("Qual seu nome? ") 
#estudante['ano_conheceu_linkedin'] = int(input("Qual o ano que conheceu o LinkedIn? "))
#estudante['ano atual'] = input("Qual é o ano atual? ")
#cursos = input("Quais cursos fez no LinkedIn Learning (separe-os com vírgula)")
#estudante['cursos'] = cursos.split(", ")

#print(estudante)
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

#total_anos = estudante["ano atual"] - estudante["ano_conheceu_linkedin"]
#total_cursos = len(estudante["cursos"])

#print(f"Olá {estudante['nome']}")

#outra abordagem

estudante = {}

while True:
    try:
        estudante['nome'] = input("Qual seu nome? ")
        if estudante['nome'].isalpha() or estudante['nome'].isspace():  # Verifica se é apenas letras ou espaços em branco
            break  # Sai do loop se for válido
        else:
            print("Erro: Digite apenas letras e espaços em branco para o nome: ")
    except ValueError:
        pass  # Ignora exceções de ValueError, pois não são relevantes para este caso

while True:
    try:
        ano_linkedin = input("Qual o ano que conheceu o LinkedIn? ")
        estudante['ano_conheceu_linkedin'] = int(ano_linkedin)
        break  # Sai do loop se for válido
    except ValueError:
        print("Erro: Digite um ano válido (apenas números): ")

while True:
    try:
        ano_atual = input("Qual é o ano atual? ")
        estudante['ano_atual'] = int(ano_atual)
        break  # Sai do loop se for válido
    except ValueError:
        print("Erro: Digite um ano válido (apenas números): ")

while True:
    cursos = input("Quais cursos fez no LinkedIn Learning (separe-os com vírgula)? ")
    try:
        cursos_lista = cursos.split(", ")  # Separa os cursos por vírgula
        if len(cursos_lista) == 0:  # Verifica se há pelo menos um curso
            print("Erro: Digite pelo menos um curso.")
            continue
        for curso in cursos_lista:  # Verifica se cada curso contém apenas letras e espaços
            if not curso.isalpha() and not curso.isspace():
                print(f"Erro: O curso '{curso}' contém caracteres inválidos. Digite apenas letras e espaços em branco.")
                continue
        estudante['cursos'] = cursos_lista  # Adiciona a lista de cursos ao dicionário
        break  # Sai do loop se tudo estiver ok
    except ValueError:
        print("Erro: Utilize vírgulas para separar os cursos.")

# Cálculo do tempo de uso do LinkedIn Learning
if int(estudante['ano_atual']) >= int(estudante['ano_conheceu_linkedin']):
    tempo_linkedin = int(estudante['ano_atual']) - int(estudante['ano_conheceu_linkedin'])
else:
    tempo_linkedin = 0

# Apresentação dos resultados
print(f"Olá {estudante['nome']}! Você está no LinkedIn Learning há {tempo_linkedin} anos (desde {estudante['ano_conheceu_linkedin']}). Seus cursos no LinkedIn Learning: ")
if 'cursos' in estudante:  # Verifica se a chave 'cursos' existe
    for curso in estudante['cursos']:
        print(f"- {curso}")
else:
    print("Você ainda não cadastrou nenhum curso.")

print("\nObrigado por usar o nosso programa!")
