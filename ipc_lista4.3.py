notas = []
v = 4
c1 = 0
c2 = 1
soma = 0

while(c1 < v):
    x = float(input("Informe a nota do %dº bimestre:\n"%c2))
    notas.append(x)
    soma+=notas[c1]
    c1+=1
    c2+=1
print("A media das notas dos quatro bimestres e de %.2f"%(soma/v))
