import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vendas.csv')

#?Ex1 - Agrupamento e soma
print("--EX1--")
group = df.groupby('Produto')['Quantidade'].sum()
print(group)

#?Ex2 - Criação de Nova Coluna com Cálculos
print("--EX2--")
df['Lucro'] = df['Preco_Unitario'] * 0.20
print(df)

#?Ex3 - Exportação para Excel
print("--EX3--")
df.to_excel('vendas_com_lucro.xlsx', index=False)

#?Ex4 - Visualização de Dados
print("--EX4--")
group = df.groupby('Produto')['Total_Venda'].sum()
group.plot(kind='bar', x='Produto', y='Total_Venda', title='Total de vendas por produtos')
plt.savefig('Graph1')
plt.show()

#?Ex5 - Ordenação de Dados
print("--EX5--")
df_sorted = df.sort_values(by="Total_Venda", ascending=False )
print(df_sorted)

#?Ex6 - Remoção de Duplicados
print("--EX6--")
df_duplicates = df.duplicated().sum()
print(df_duplicates)
df_wout_duplicates = df.drop_duplicates()
print(df_wout_duplicates)

#?Ex7 - Aplicação de Função Personalizada
print("--EX7--")
def apply_discount(price):
    return price * 0.90
    
df['Preco_Ajustado'] = df['Preco_Unitario'].apply(apply_discount)
print(df)

#?Ex8 - Análise de séries Temporais
print("--EX8--")
df['Data'] = pd.to_datetime(df['Data'])
df = df.set_index(keys='Data')
group = df['Total_Venda'].resample('M').sum()
group.plot(kind='line', x="Data", y="Total_Venda", title='Vendas Por Tempo')
plt.savefig('Graph2')
plt.show()

"""
?Qual é a tendência geral das vendas ao longo do tempo?

As vendas começam altas em janeiro, mas caem consistentemente até março.
Em abril e maio, há uma recuperação moderada, seguida de uma descida acentuada até julho.

?Existem padrões sazonais ou flutuações nos dados?

A tendência geral é de queda ao longo do período.
Observam-se flutuações, mas não é possível identificar um padrão sazonal claro com os dados disponíveis.
"""

