import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(valores):
    plt.hist(valores, bins=np.arange(min(valores), max(valores)+2), alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Soma dos dados')
    plt.ylabel('Contagem')
    plt.title('Histograma')
    plt.tight_layout()
    plt.show()

def jogar_dados(num_dados, num_vezes):
    dados = np.random.choice([1, 2, 3, 4, 5, 6], size=(num_vezes, num_dados))
    soma_dados = dados.sum(axis=1)
    return soma_dados

num_dados = 100
num_vezes = 10000000
valores = jogar_dados(num_dados, num_vezes)

plot_histogram(valores)
#
