import pandas as pd
import matplotlib.pyplot as plt

# Ler dados do arquivo CSV
file_path = 'shopping_trends.csv'
df = pd.read_csv(file_path)

# Calcular a compra média por idade
average_purchase_by_age = df.groupby('Age')['Purchase Amount (USD)'].mean()

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(average_purchase_by_age, marker='o', color='skyblue')
plt.title('Compra Média por Idade')
plt.xlabel('Idade')
plt.ylabel('Compra Média (USD)')
plt.grid(True)
plt.show()
