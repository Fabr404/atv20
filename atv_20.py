# Crie um programa que utilize uma estrutura de repetição para somar todos os números pares de 1 a 100 e exiba o resultado.

soma = 0

# Loop para percorrer os números de 1 a 100

for numero in range(1, 101):
    if numero % 2 == 0: 
        soma += numero 

# exibir resultado

print("A soma de todos os números pares de 1 a 100 é:", soma)