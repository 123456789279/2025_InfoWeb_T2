#Fase 1
#Idade de Camila
Cibele = int(input())
Camila = int(input())
Celeste = int(input())
x = [Cibele, Camila, Celeste]
x.sort()
print(x[1])

#Tempo de resposta
n = int(input())









#Zero para cancelar
n = int(input())
lista = []
for k in range(n):
    x = int(input())
    if x != 0: lista.append(x)
    else: lista.pop()
if len(lista) == 0: print(0)
else: print(sum(lista))
