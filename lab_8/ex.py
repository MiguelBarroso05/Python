import pandas as pd
import matplotlib.pyplot as plt

#? Criar uma Series com rotulos personalizados
dados = pd.Series ([10, 20, 30], index=['a', 'b', 'c'])
print(dados, "\n" + "-"*30)

#? Criar um DataFrame a partir de um dicionario
dados = {'Produto': ['Produto A', 'Produto B', 'Produto C'],
'Preco': [10.5, 22.3, 19.99] ,
'Quantidade': [5, 3, 10]}
df = pd.DataFrame(dados)
print(df , "\n" + "-"*30)

#? Selecionar a coluna "Produto"
produtos = df['Produto']
print(produtos, "\n"+ "-"*30)

#? Selecionar uma linha especifica utilizando o rotulo
linha_b = df.loc[1]
print(linha_b, "\n"+ "-"*30)

#? Filtrar os produtos cujo Preco superior a 20
filtro = df[df['Preco'] > 20]
print(filtro, "\n"+ "-"*30)

#? Criar um DataFrame com dados em falta
dados = {'Produto': ['Produto A', 'Produt B', 'Produto C'],
'Preco': [10.5, None , 19.99] ,
'Quantidade': [5, 3, None]}
df = pd.DataFrame(dados)

#? Verificar dados em falta
print(df.isnull (), "\n"+ "-"*30)

#? Substituir dados em falta
df_filled = df.fillna (0)
print(df_filled, "\n"+ "-"*30)

#? Agrupar dados por "Produto" e somar as quantidades
grupo = df.groupby('Produto').sum()
print(grupo, "\nAQUIII"+ "-"*30)

#? Criar dois DataFrames
df1 = pd.DataFrame ({'Produto': ['Produto A', 'Produto B'],
'Preco': [10.5, 22.3]})
df2 = pd.DataFrame ({'Produto': ['Produto A', 'Produto B'],
'Quantidade ': [5, 3]})

#? Juntar os DataFrames com base na coluna "Produto"
df_merged = pd.merge(df1 , df2 , on='Produto')
print(df_merged, "\n"+ "-"*30)

#? Preencher valores NaN em 'Preco' e 'Quantidade ' com 0 para evitar NaN no resultado
df['Valor_Total'] = df['Preco']. fillna (0) * df['Quantidade']. fillna (0)

#? Adicionar uma nova coluna "Soma_Preco_Quantidade" com a soma de 'Preco' e 'Quantidade ',
#?tratando NaNs
df['Soma_Preco_Quantidade'] = df['Preco']. fillna (0) + df['Quantidade']. fillna (0)
print(df, "\n"+ "-"*30)

#? Exportar o DataFrame para um ficheiro Excel
df.to_excel('dados_produtos.xlsx', index=False)

#? Criar um grqfico de barras para a quantidade de produtos
df.plot(kind='bar', x='Produto', y='Quantidade', title='Quantidade de Produtos')

#? Mostrar o grafico
plt.show()

#? Ordenar o DataFrame pelo valor da coluna 'Preco '
df_sorted = df.sort_values(by='Preco', ascending=False)
print(df_sorted)

#? Remover linhas duplicadas no DataFrame
df_unique = df.drop_duplicates ()
print(df_unique)

#? Aplicar uma funcao que aumenta o preco em 10%
df['Preco_Ajustado'] = df['Preco']. apply(lambda x: x * 1.10)
print(df)