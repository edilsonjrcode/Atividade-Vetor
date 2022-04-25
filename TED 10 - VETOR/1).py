print("""1) Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa""")

print("\n\033[1;31mVETOR")
print("\033[30m")

vet = []
cont = 1

while cont <= 20:
  num = int(input("Digite o {}° número: ".format(cont)))
  vet.append(num)
  cont += 1
print("\nVetor =",vet)
vet.reverse()
print("Vetor Invertido =",vet)


