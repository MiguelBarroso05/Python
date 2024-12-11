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
    
