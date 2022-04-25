print("""\n2) Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.""")
print("\033[1;31mVETOR")

print("\nMODO MANUAL""\033[3;30m")

vet = []
rep = []
i = 0
j = 0

while i <= 49:
  num = int(input("Digite o {}° número: ".format(i+1)))
  vet.append(num)
  rep.append(i)
  i += 1
  if vet.count(num) > 1:
    print("O número {} está se repetindo no índice {}".format(num, i))
    j += 1
print("\nVetor =", vet)
print("A lista possui {} número(s) repetidos.".format(j))

