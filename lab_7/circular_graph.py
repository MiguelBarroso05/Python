import pandas as pd
import matplotlib.pyplot as plt

#Carregar o ficheiro CSV
df = pd.read_csv('vendas_loja.csv')

#Calcular as vendas totais por produto
vendas_totais = df.groupby('Produto')['Total_Venda'].sum()

#Criar o gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(vendas_totais, labels=vendas_totais.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab10.colors)

#Título
plt.title('Proporção das Vendas Totais por Produto')

#Gráfico
plt.tight_layout()
plt.show()