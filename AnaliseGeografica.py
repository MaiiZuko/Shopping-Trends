#Esse gráfico de barras permite vizualizar a quantidade de vendas por estados, limitandos por 20 resultados
import pandas as pd
import matplotlib.pyplot as plt 

arq = pd.read_csv('shopping_trends_updated.csv')


venda_por_estado = arq.groupby('Location')['Purchase Amount (USD)'].sum()


limite = 20
venda_por_estado_limite = venda_por_estado.head(limite)


plt.bar(venda_por_estado_limite.index, venda_por_estado_limite, color='#87CEEB')
plt.xlabel('Estado')
plt.ylabel('Contagem')
plt.title(f'Top {limite} Estados por Número de Vendas')
plt.xticks(rotation=45, ha='right')
for i, valor in enumerate(venda_por_estado_limite):
    plt.text(venda_por_estado_limite.index[i], valor, str(round(valor, 2)),
             ha='center', va='bottom', fontsize=9, color='black')

plt.show()   