## Fa�a um programa que gere dois vetores, um com valores aleat�rios e outro digitado e mostrar os itens em comum

import random

posi��o = 0
num = int(input("Digite o tamanho dos vetores..:"))
vet = []
vet2 = []

for x in range(num):
    vet2.append(random.randrange(1, 9))

for i in range(num):
    x = float(input("Digite os valores do vetor:"))
    vet.append(x)
    posi��o += 1

if vet[i] == vet2[i]:
    print('O valor ', vet[i], " esta presente nos dois vetores e sua posi��o �..:", posi��o)

else:
    print('Na posi��o ', posi��o, "os valores s�o diferentes")