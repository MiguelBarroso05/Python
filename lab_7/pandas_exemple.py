import pandas as pd
 
# Carregar o ficheiro CSV
df = pd.read_csv('vendas_loja.csv')
    
    # Verificar a existencia de valores nulos em todas as colunas
print("Valores nulos por coluna antes do preenchimento:")
print(df.isna().sum())
    
# Preencher valores nulos na coluna "Quantidade" com a media dessa coluna
df['Quantidade'].fillna(df['Quantidade'].mean(), inplace=True)
    
# Preencher valores nulos na coluna "Preco_Unitario" com a media dessa coluna
df['Preço_Unitario'].fillna(df['Preço_Unitario'].mean(), inplace=True)
    
# Adicionar uma nova coluna "coluna_numerica" como exemplo (calculando Total a partir de Quantidade * Preco_Unitario)
df['coluna_numerica'] = df['Quantidade'] * df['Preço_Unitario']
    
# Preencher valores nulos na nova coluna "coluna_numerica" (se houver)
df['coluna_numerica'].fillna(df['coluna_numerica'].mean(), inplace=True)
    
# Verificar novamente se ha valores nulos apos o preenchimento
print("\nValores nulos por coluna apos o preenchimento:")
print(df.isna().sum())
    
# Exibir as primeiras linhas do DataFrame atualizado
print("\nPrimeiras linhas do DataFrame atualizado:")
print(df.head())
    
# Guardar o DataFrame atualizado num novo ficheiro CSV
df.to_csv('vendas_loja_atualizado.csv', index=False)