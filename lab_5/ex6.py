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