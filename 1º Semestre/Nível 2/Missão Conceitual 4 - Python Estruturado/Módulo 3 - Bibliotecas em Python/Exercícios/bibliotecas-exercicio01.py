# Implementar uma solução em Python para visualizar dados de vendas de produtos em um gráfico de barras.
# Por exemplo, utilize os seguintes dados:
# x = ["A", "B", "C", "D"]
# y = [3, 8, 1, 10]

import matplotlib.pyplot as plt          # Para dizer que quero trabalhar com gráfico de barras
import numpy as np                       # numpy para entrada de dados

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()
