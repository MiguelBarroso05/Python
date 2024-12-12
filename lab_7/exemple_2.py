import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Carregar o ficheiro CSV
df = pd.read_csv('vendas_loja.csv')
# Configurar o estilo do seaborn
sns.set_theme(style='whitegrid')
# Criar um grafico de barras para visualizar as vendas por produto
plt.figure(figsize =(10, 6))
sns.barplot(x='Produto', y='Total_Venda', data=df, estimator=sum)
plt.title('Total de Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.xticks(rotation =45)
plt.tight_layout ()
# Exibir o grafico
plt.show()
# Criar um grafico de dispersao para visualizar a relacao entre Preço_Unitário e
#Quantidade Vendida
plt.figure(figsize =(10, 6))
sns.scatterplot(x='Preço_Unitario', y='Quantidade', data=df, hue='Produto', palette='deep')
plt.title('Relacao entre Preço_Unitário e Quantidade Vendida ')
plt.xlabel('Preço_Unitário')
plt.ylabel('Quantidade Vendida')
plt.legend(title='Produto')
plt.tight_layout ()
# Exibir o grafico
plt.show()
# Criar um grafico de linhas para visualizar a tendencia de vendas ao longo do tempo
df['Data'] = pd.to_datetime(df['Data']) # Converter a coluna 'Data' para o formato de data
plt.figure(figsize =(10, 6))
sns.lineplot(x='Data', y='Total_Venda', data=df, marker='o')
plt.title('Tendencia de Vendas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Total de Vendas')
plt.xticks(rotation =45)
plt.tight_layout ()
# Exibir o grafico
plt.show()