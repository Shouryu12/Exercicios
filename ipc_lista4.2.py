lista1 = []
lista2 = []
v = 10
c1 = 0
c2 = 1

while c1 < v:
    x = float(input("Informe o %dº numero para colocar em sua lista:\n"%c2))
    lista1.append(x)
    c1+=1
    c2+=1
i = len(lista1)-1
print(lista1)

while i >= 0:
    y = lista1[i]
    lista2.append(y)
    i= i-1
print("A lista invertida é:\n%s"%lista2)