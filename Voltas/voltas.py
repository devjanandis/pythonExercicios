volta = []

temp = 99999
p = 0
tm = 0
tempomed = 0

for i in range(5):
    volta.append(float(input("Informe o tempo da volta: ")))
    tm += volta[i]

for i in range(5):
    if volta[i] < temp:
        temp = volta[i]
        p = i
        tempomed = tm/(i+1)

print(volta)
print("A melhor volta teve: ", temp, " minutos")
print("E ocorreu na seguinte volta: ", p+1)
print("O tempo médio das voltas da corrida foi de ", tempomed, " minutos")