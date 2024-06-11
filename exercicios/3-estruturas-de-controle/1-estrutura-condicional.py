# Declare 4 variáveis do tipo numérica
a = 10
b = 11
c = 12
d = 13
e = 14
f = 15


# Crie uma estrutura condicional para comparar dois números
#if x > y :
#  print(f"x > y - Condição atendida {x} é maior do que {y}")
#elif x > a :
#  print(f"x > a - Condição atendida {x} é maior do que {a}")
#else:
#  print("x > y - Condição não atendida")

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor


# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor


# Insira outras condições na estrutura condicional usando o elif


# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"


# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
print("#################################")

while True:
    try:
        texto = input("Digite um número de 0 - 16: ")
        numero = int(texto)

        if 0 <= numero <= 16:
            # Use hex() function for efficient conversion
            hex_value = hex(numero).upper()[2:]  # Remove "0x" prefix and uppercase letters
            print("#################################")
            print(f"Número decimal: {numero}")
            print(f"Número hexadecimal: {hex_value}")
            break  # Exit the loop after successful input

        else: # basta substituir o else pelo if e a condição para continuar o exercício
            #porém essa solução já atende ao propósito do meu código
            print("#################################")
            print("O número deve estar entre 0 e 16. Tente novamente.")

    except ValueError:
        print("#################################")
        print("Entrada inválida. Digite um número inteiro.")

print("#################################")
