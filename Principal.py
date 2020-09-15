from model import GrafoMain as gm

g = {"a": ["d","e"],
     "b": ["c"],
     "c": ["b", "c", "d", "e"],
     "d": ["a", "c"],
     "e": ["c"],
     "f": []
     }

grafo = gm.Grafo(g)

print(grafo)
print("Vértices isolados:")
print(grafo.vertices_isolados())
print("Caminho de a até e:")
print(grafo.achar_caminho("a","e"))
print("Caminhos de a até e:")
print(grafo.achar_todosCaminhos("a","e"))