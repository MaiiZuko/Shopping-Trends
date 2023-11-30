# formas de pagamentos mais escolhidos pelos clientes - gráfico de pizza

import pandas as pd
import matplotlib.pyplot as plt

st = pd.read_csv("shopping_trends.csv")

# contagem da frequência de cada método de pagamento
contagem_formas_pagamento = st["Payment Method"].value_counts()

# criação do gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(
    contagem_formas_pagamento,
    labels=contagem_formas_pagamento.index,
    startangle=140,
    autopct=lambda p: "{:.0f}".format(p * contagem_formas_pagamento.sum() / 100),
    shadow=True,
)

plt.title("Formas de Pagamento")

plt.show()
