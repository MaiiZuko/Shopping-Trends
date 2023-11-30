# formas de pagamento realizadas em cada tipo de frete - gráfico de barras

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("shopping_trends.csv")

sns.set(style="whitegrid")

plt.figure(figsize=(12, 8))
sns.countplot(x="Shipping Type", hue="Payment Method", data=df)

plt.title("Relação entre Tipos de Frete e Formas de Pagamento")
plt.xlabel("Tipos de Frete")
plt.ylabel("Quantidade")
plt.legend(loc="lower right")

plt.show()
