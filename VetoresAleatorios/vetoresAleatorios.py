## Faça um programa que gere dois vetores, um com valores aleatórios e outro digitado e mostrar os itens em comum

import random

posição = 0
num = int(input("Digite o tamanho dos vetores..:"))
vet = []
vet2 = []

for x in range(num):
    vet2.append(random.randrange(1, 9))

for i in range(num):
    x = float(input("Digite os valores do vetor:"))
    vet.append(x)
    posição += 1

if vet[i] == vet2[i]:
    print('O valor ', vet[i], " esta presente nos dois vetores e sua posição é..:", posição)

else:
    print('Na posição ', posição, "os valores são diferentes")