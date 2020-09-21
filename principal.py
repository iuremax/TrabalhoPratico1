import grafinho as g
grafo = g.Grafo()
def menu():
  opc = 0
  print("Criando um Grafo\n")
  while opc != 6:
    opc = int(input("1 - Criar Vértices\n""2 - Criar Arestas\n""3 - Listar Vértices\n""4 - Listar Arestas\n""5 - Imprimir Grafo\n""6 - Sair\n""Selecionar :"))
    if opc == 1:
      print()
      grafo.adicionar_vertice(input("Adicione um vértice: "))
      print()
    elif opc == 2:
      print()
      grafo.adicionar_aresta(input("Adicione uma aresta: "))
      print()
    elif opc == 3:
      print()
      print(grafo.vertices())
      print()
    elif opc == 4:
      print()
      print(grafo.arestas())
      print()
    elif opc == 5:
      print()
      print(grafo)
      print()
menu()
