from random import randint

print("\n\033[1;31m""                         MATRIZ""\033[0;33m\n")

a = []
i = soma = 0
for l in range(0, 10):
  n = []
  for c in range(0, 10):
    num = randint(10, 99)
    soma = soma+num
    n.append(num)
  print("      ", n)
  i += 1
  a.append(n)

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

soma2 = 0
for lin in a:
  for col in lin:
    soma2 = soma2+col
print(
    "\n\033[1;31m"f"\nA soma de todos os números da matriz é igual a {soma2}""\033[0;33m\n")

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


print("\n\033[1;31m""                      MATRIZ * 3""\033[0;30m\n")

b = []
for lin in a:
  c = []
  for col in lin:
    num_3 = col*3
    c.append(num_3)
  b.append(c)
  print("\033[0;33m\n""    ", c)

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
