nota1 = int(input('Digite sua nota: '))
nota2 = int(input('Digite sua 2° nota: '))

nota = (nota1 + nota2) / 2

if nota >= 7 and nota < 10:     
    print ("Aprovado!") 
elif nota >= 10:
    print ("Você foi Aprovado")
else:
    print ("Reprovado")