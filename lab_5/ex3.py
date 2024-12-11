age = int(input("What's your age?\n"))
if (16 <= age <= 18):
    print("You can drive")
elif (18 < age < 21):
    print("You can vote")
elif (21 <= age ):
    print("You can DRINK VODKA")
else:
    print("Continue studying")
 
"""
Que estrutura condicional seria mais eficiente para implementar 
este exercício: múltiplos if-else ou outra abordagem?


A estrutura condicional mais eficiente seria a de múltiplos if-else, 
pois permite verificar de forma clara e concisa as diferentes faixas 
etárias. No entanto, usar if-elif-else como já está no código é uma 
abordagem adequada, pois permite evitar a execução desnecessária de 
múltiplas condições após a primeira que for verdadeira.

Que regras podem variar de país para país? Como poderia adaptar 
o programa para suportar diferentes legislações?

As regras podem variar, por exemplo, em relação à idade mínima para dirigir, 
votar ou consumir álcool, dependendo do país. Para adaptar o programa a 
diferentes legislações, seria interessante adicionar uma opção para o 
usuário escolher o país ou permitir a configuração das idades específicas 
conforme a legislação local, ajustando as condições conforme as leis 
vigentes em cada região.
"""