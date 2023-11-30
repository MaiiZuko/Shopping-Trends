import pandas as pd
import matplotlib.pyplot as plt

file_path = 'shopping_trends.csv'
df = pd.read_csv(file_path)

fig, axes = plt.subplots(1, 3, figsize=(18, 5)) #subplots

#itens mais populares - gráfico de linha
popular_items = df['Item Purchased'].value_counts().nlargest(5)
axes[0].plot(popular_items.index, popular_items.values, marker='o', linestyle='-', color='skyblue')
axes[0].set_title('Itens Mais Populares')
axes[0].set_xlabel('Item')
axes[0].set_ylabel('Número de Compras')

#itens menos populares - gráfico de linha
unpopular_items = df['Item Purchased'].value_counts().nsmallest(5)
axes[1].plot(unpopular_items.index, unpopular_items.values, marker='o', linestyle='-', color='lightcoral')
axes[1].set_title('Itens Menos Populares')
axes[1].set_xlabel('Item')
axes[1].set_ylabel('Número de Compras')

# distribuição de cores dos itens - gráfico de pizza
color_count = df['Color'].value_counts()
axes[2].pie(color_count, labels=color_count.index, autopct='%1.1f%%', startangle=90)
axes[2].set_title('Distribuição de Cores dos Itens')
axes[2].axis('equal') 

plt.tight_layout()
plt.show()
