class Grafo(object):

    def __init__(self, grafo_dicionario=None):
        """ initializa um objeto grafo, se nenhum dicionário ou "None" é dado, um dicionário vazio será usado"""
        if grafo_dicionario == None:
            grafo_dicionario = {}
        self.__grafo_dicionario = grafo_dicionario

    def vertices(self):
        """ retorna os vértices do grafo """
        return list(self.__grafo_dicionario.keys())

    def arestas(self):
        """ retorna as arestas do grafo """
        return self.__gerar_arestas()

    def adicionar_vertice(self, vertice):
        """ Se o vértice "vertice" nõ estiver em self.__grafo_dicionario, uma key "vertice" com uma
            lista vazia como um valor é adicionado ao dicionário. Caso contrário, nada é feito."""
        if vertice not in self.__grafo_dicionario:
            self.__grafo_dicionario[vertice] = []

    def adicionar_aresta(self, aresta):
        """ assume que a aresta é do tipo set, tuple ou list; entre dois vértices podem existir múltiplas arestas!"""
        aresta = set(aresta)
        (vertice1, vertice2) = tuple(aresta)
        if vertice1 in self.__grafo_dicionario:
            self.__grafo_dicionario[vertice1].append(vertice2)
        else:
            self.__grafo_dicionario[vertice1] = [vertice2]

    def __gerar_arestas(self):
        """ Um método estático gerando as arestas do grafo "grafo". Arestas são representadas como sets
            com um (um laço) ou dois vértices."""
        arestas = []
        for vertice in self.__grafo_dicionario:
            for neighbour in self.__grafo_dicionario[vertice]:
                if {neighbour, vertice} not in arestas:
                    arestas.append({vertice, neighbour})
        return arestas

    def __str__(self):
        res = "vértices: "
        for k in self.__grafo_dicionario:
            res += str(k) + " "
        res += "\narestas: "
        for aresta in self.__gerar_arestas():
            res += str(aresta) + " "
        return res

    def vertices_isolados(self):
        """ retorna uma lista de vértices isolados """
        grafo = self.__grafo_dicionario
        isolado = []
        for vertice in grafo:
            print(isolado, vertice)
            if not grafo[vertice]:
                isolado += [vertice]
        return isolado

    def achar_caminho(self, vertice_inicial, vertice_final, caminho=[]):
        """ encontra um caminho de um vertice_inicial até um vertice_final no grafo"""
        grafo = self.__grafo_dicionario
        caminho = caminho + [vertice_inicial]
        if vertice_inicial == vertice_final:
            return caminho
        if vertice_inicial not in grafo:
            return None
        for vertice in grafo[vertice_inicial]:
            if vertice not in caminho:
                extended_caminho = self.achar_caminho(vertice, vertice_final, caminho)
                if extended_caminho:
                    return extended_caminho
        return None

    def achar_todosCaminhos(self, vertice_inicial, vertice_final, caminho=[]):
        """ encontra todos os caminhos de um vertice_inicial até um vertice_final no grafo"""
        grafo = self.__grafo_dicionario
        caminho = caminho + [vertice_inicial]
        if vertice_inicial == vertice_final:
            return [caminho]
        if vertice_inicial not in grafo:
            return []
        caminhos = []
        for vertice in grafo[vertice_inicial]:
            if vertice not in caminho:
                extended_caminhos = self.achar_todosCaminhos(vertice, vertice_final, caminho)
                for p in extended_caminhos:
                    caminhos.append(p)
        return caminhos