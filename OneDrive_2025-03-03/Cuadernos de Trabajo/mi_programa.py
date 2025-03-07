
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

n_tiradas = 600
tirosdados = [random.randint(1, 6) for _ in range(n_tiradas)]
val, frecuencias = np.unique(tirosdados, return_counts=True)

sns.set_style("whitegrid")
fig, axes = plt.subplots()
axes.bar(val, frecuencias, color=['orange', 'green', 'red', 'purple', 'brown', 'blue'])
axes.set_title(f"Resultados de tirar los dados {n_tiradas} veces")
axes.set_xlabel("Valores")
axes.set_ylabel("Frecuencias")

for bar, freq in zip(axes.patches, frecuencias):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{freq:,}\n{freq/len(tirosdados):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

plt.show()
