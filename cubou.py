import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir os vértices do cubo
vertices = np.array([
    [-1, -1, -1],  # Vértice 0
    [1, -1, -1],   # Vértice 1
    [1, 1, -1],    # Vértice 2
    [-1, 1, -1],   # Vértice 3
    [-1, -1, 1],   # Vértice 4
    [1, -1, 1],    # Vértice 5
    [1, 1, 1],     # Vértice 6
    [-1, 1, 1]     # Vértice 7
])

# Definir as arestas conectando os vértices
arestas = [
    [0, 1], [1, 2], [2, 3], [3, 0],  # Base inferior
    [4, 5], [5, 6], [6, 7], [7, 4],  # Base superior
    [0, 4], [1, 5], [2, 6], [3, 7]   # Conectando inferior e superior
]

def plot_cubo(vertices, arestas):
    """Função para desenhar o cubo."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plotar os vértices
    for v in vertices:
        ax.scatter(v[0], v[1], v[2], color='red')

    # Plotar as arestas conectando os vértices
    for edge in arestas:
        v0, v1 = vertices[edge[0]], vertices[edge[1]]
        ax.plot([v0[0], v1[0]], [v0[1], v1[1]], [v0[2], v1[2]], color='blue')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Cubo 3D')
    plt.show()

# Exibir o cubo
plot_cubo(vertices, arestas)
