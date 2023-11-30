#Esse gráfico análisa a quantidade de venas por estações do ano

import pandas as pd
import matplotlib.pyplot as plt


arq = pd.read_csv('shopping_trends_updated.csv')  


vendas_estacao = arq.groupby('Season')['Purchase Amount (USD)'].sum()


plt.plot(vendas_estacao.index, vendas_estacao, color='#000080', marker='o', linestyle=':', linewidth=2)

plt.xlabel('Estação')
plt.ylabel('Vendas Totais (USD)') 
plt.title('Vendas Totais por Estação')
plt.grid(True)


plt.show() 
