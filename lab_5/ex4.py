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