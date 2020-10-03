class Grafo(object):

    def __init__(self, grafo_dicionario=None):
        #initializa um objeto grafo na forma de dicionário
        if grafo_dicionario == None:
            grafo_dicionario = {}
        self.__grafo_dicionario = grafo_dicionario

    def vertices(self):
        #retorna os vertices
        return list(self.__grafo_dicionario.keys())

    def arestas(self):
        #retorna as arestas
        return self.__gerar_arestas()

    def adicionar_vertice(self, vertice):
        if vertice not in self.__grafo_dicionario:
            self.__grafo_dicionario[vertice] = []

    def adicionar_aresta(self, aresta):
        aresta = set(aresta)
        (vertice1, vertice2) = tuple(aresta)
        if vertice1 in self.__grafo_dicionario:
            self.__grafo_dicionario[vertice1].append(vertice2)
        else:
            self.__grafo_dicionario[vertice1] = [vertice2]

    def __gerar_arestas(self):
        arestas = []
        for vertice in self.__grafo_dicionario:
            for neighbour in self.__grafo_dicionario[vertice]:
                if {neighbour, vertice} not in arestas:
                    arestas.append({vertice, neighbour})
        return arestas

    def __str__(self):
        #retorna o grafo completo
        res = "vértices: "
        for k in self.__grafo_dicionario:
            res += str(k) + " "
        res += "\narestas: "
        for aresta in self.__gerar_arestas():
            res += str(aresta) + " "
        return res
