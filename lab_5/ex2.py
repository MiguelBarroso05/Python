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
