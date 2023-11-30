import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'shopping_trends.csv'  #le arquivo CSV
df = pd.read_csv(file_path)

fig, axes = plt.subplots(1, 2, figsize=(15, 10))  #subplots

#analisa a distribuição etária dos clientes
sns.histplot(df['Age'], bins=20, kde=True, ax=axes[0])
axes[0].set_title('Distribuição Etária dos Clientes')
axes[0].set_xlabel('Idade')
axes[0].set_ylabel('Frequência')

#analisa a relação entre a idade e o valor médio de compra
age_purchase_mean = df.groupby('Age')['Purchase Amount (USD)'].mean()
age_purchase_mean.plot(marker='o', ax=axes[1])
axes[1].set_title('Relação entre Idade e Valor Médio de Compra')
axes[1].set_xlabel('Idade')
axes[1].set_ylabel('Valor Médio de Compra (USD)')

#ajusta layout e mostrar os subplots
plt.tight_layout()
plt.show()
