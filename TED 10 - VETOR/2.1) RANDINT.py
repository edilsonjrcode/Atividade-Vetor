import random
print(
    """\n\033[1;31m2) Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.""")

print("\nVETOR""\033[3;37m\n")

vet = []
rep = []
i = 0
j = 0

while i <= 49:
    num = random.randint(1, 50)
    vet.append(num)
    rep.append(i)
    i += 1
    if vet.count(num) > 1:
        print("O número {} está se repetindo no índice {}".format(num, i))
        j += 1
print("\nVetor =", vet)
print("\nA lista possui {} número(s) repetidos.".format(j))
