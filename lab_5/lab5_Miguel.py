#ex1

import random
winner_number = random.randint(1,100)
number_of_tries = 0
while True:
    number_of_tries += 1
    guess = int(input("Guess a number?\n"))
    if(guess == winner_number):
        print("You win!")
        break
    elif(guess < winner_number):
        print("Too low!")
    else:
        print("Too high!")
"""
De que forma a função random.randint() gera números aleatórios?

    A função random.randint() gera números aleatórios inteiros dentro
    de um intervalo especificado, usando o gerador de números pseudo-aleatórios
    da biblioteca random.
    
O que aconteceria se o utilizador introduzisse um valor inválido
(não numérico)? Como poderia tratar essa situação?

    Se o utilizador introduzir um valor não numérico, ocorre um erro.
    Para tratar, pode-se usar try-except para capturar e tratar exceções
    de entrada inválida.
"""
    


#ex2

def calculate_simple_interest(capital, interest, years):

    return capital * (interest / 100) * years
def  calculate_compound_interest(capital, interest, years):
    return  capital * (1 + interest / 100) * years

capital = int(input("Insert your initial capital: "))
interest = int(input("Insert the interest rate: "))
years = int(input("Insert the amount of years you want to invest: "))

simple_interest = calculate_simple_interest(capital, interest, years)
compound_interest = calculate_compound_interest(capital, interest, years)
print(f"The simple interest is {simple_interest:.2f}$")
print(f"The compound interest is {compound_interest:.2f}$")

"""
Qual é a fórmula para o cálculo de juros simples? E para juros compostos?

A fórmula dos juros simples é: J=P×i×t, onde J são os juros, 
P é o capital inicial, 
i é a taxa de juro e 
t é o tempo em anos. O montante total após o período é dado por 
M=P×(1+i×t). Os juros simples são calculados apenas sobre o valor inicial.

Qual seria a melhor opção de investimento dependendo da taxa de juro e do 
número de anos?

Juros Simples são mais vantajosos para períodos curtos, pois os juros 
são calculados apenas sobre o valor inicial.
Juros Compostos são mais vantajosos para investimentos de longo prazo, 
pois os juros são calculados sobre o montante acumulado, o que gera 
"juros sobre juros", aumentando exponencialmente o valor investido.
"""


#ex3

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

#ex4

import random


math_signs = ["+","-","*","/"]
first_number = random.randint(1, 20)
second_number = random.randint(1, 20)
sign_randomizer = random.randint(0, len(math_signs) - 1)
match math_signs[sign_randomizer]:
    case "+":
        result = first_number + second_number
    case "-":
        result = first_number - second_number
    case "*":
        result = first_number * second_number
    case "/":
        result = first_number / second_number
print(f" {first_number}  {math_signs[sign_randomizer]}  {second_number}")
user_guess = int(input("What is the result of the calculation?\n"))
while user_guess != result:
    user_guess = int(input("WRONG!!\nWhat is the result of the calculation?\n"))

print(f"You won the result is {result}")

"""
Como pode garantir que as operações geradas são equilibradas, 
ou seja, que não são demasiado fáceis ou difíceis?

Para equilibrar as operações, evitar divisões com resultados
decimais e ajustar os números conforme o nível de dificuldade.

Como pode o programa fornecer feedback ao utilizador sobre o seu 
progresso ou desempenho?

Mostrar o número de tentativas ou acertos, e incentive o 
usuário com mensagens após várias tentativas erradas.
"""

#ex5

users = [
    {"username": "admin", "password": "admin123"},
    {"username": "admin", "password": "admin123"},
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "guest", "password": "guest123"},
]
username_client = input("Enter your username: ")
password_client = input("Enter your password: ")

if any(user["username"] == username_client and user["password"] == password_client for user in users):
    print("Welcome back!")
else:
    print("Credentials invalids.")

"""
Como pode guardar os utilizadores de forma segura, evitando o uso direto de palavras-passe em
texto simples?


Para guardar as palavras-passe de forma segura, deve-se usar técnicas de hashing, como bcrypt ou Argon2, 
em vez de armazená-las em texto simples. Isso garante que mesmo que a base de dados seja comprometida, 
as palavras-passe não sejam acessíveis.

Como poderia melhorar este sistema de login para suportar funcionalidades como a recuperação de
senha ou múltiplas tentativas?

Para melhorar o sistema de login, pode-se implementar um limite de tentativas falhadas para prevenir 
ataques de força bruta, e permitir a recuperação de senha através de um link enviado ao e-mail do 
utilizador, onde o utilizador pode redefinir a senha.
"""

#ex6

year = int(input("Enter a year: "))

if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")

"""
Porque é que existem anos bissextos? Qual a importância dessa correção no calendário?

Os anos bissextos existem para corrigir a diferença entre o ano calendário e o ano solar.
Um ano solar, ou o tempo que a Terra leva para orbitar o Sol, é aproximadamente 365,2422 dias.
O ano bissexto adiciona um dia extra (29 de fevereiro) a cada quatro anos para compensar a fração
de dia perdida, garantindo que as estações do ano permaneçam alinhadas com o calendário.


Como poderia adaptar este programa para verificar um intervalo de anos?

Para adaptar o programa para verificar um intervalo de anos, pode-se pedir ao usuário para 
nserir um ano inicial e um ano final, e então usar um loop para verificar se cada ano no 
intervalo é bissexto.
"""