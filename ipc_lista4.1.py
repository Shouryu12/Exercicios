lista = [0,0,0,0,0]
c1 = 0
v = len(lista)
c2 = 1

while c1 < v:
    lista[c1] = int(input("Informe o %dº numero inteiro para colocar em sua lista:\n"%c2))
    c1+=1
    c2+=1
print lista