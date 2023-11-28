import pandas as pd
import matplotlib.pyplot as plt

# Ler dados do arquivo CSV
file_path = 'shopping_trends.csv'
df = pd.read_csv(file_path)

# Visualizar as primeiras linhas do DataFrame
print("Visualizando as primeiras linhas do DataFrame:")
print(df.head())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# Gráfico de linha: Categoria x Média do Valor da Compra
avg_purchase_by_category = df.groupby('Category')['Purchase Amount (USD)'].mean()
avg_purchase_by_category.sort_values().plot(kind='line', marker='o', color='skyblue')
plt.title('Média do Valor da Compra por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Média do Valor da Compra (USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
# Gráfico de barras: Categoria x Média do Valor da Compra
##avg_purchase_by_category = df.groupby('Category')['Purchase Amount (USD)'].mean()
#avg_purchase_by_category.plot(kind='bar', rot=45, color='skyblue')
#plt.title('Média do Valor da Compra por Categoria')
#plt.xlabel('Categoria')
#plt.ylabel('Média do Valor da Compra (USD)')
#plt.show()
