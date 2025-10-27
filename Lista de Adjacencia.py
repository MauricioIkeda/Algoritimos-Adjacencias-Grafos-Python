class Grafo():
    def __init__(self, vertice, direcional):
        self.ListaAdjacencia = {vertice: []}
        self.direcional = direcional

    def ExibirGrafos(self):
        print("Grafinho Lindo:")
        for vertice in self.ListaAdjacencia:
            print(f"{vertice} - {self.ListaAdjacencia.get(vertice)}")
        print()

    def AddVertice(self, vertice):
        self.ListaAdjacencia[vertice] = []
    
    def AddAresta(self, vertice1, vertice2):
        self.ListaAdjacencia[vertice1].append(vertice2)

        if self.direcional:
            self.ListaAdjacencia[vertice2].append(vertice1)

    def RemoverVertice(self, verticeRemover):
        self.ListaAdjacencia.pop(verticeRemover)

        if self.direcional:
            for vertice in self.ListaAdjacencia.keys():
                if verticeRemover in self.ListaAdjacencia[vertice]:
                    self.ListaAdjacencia[vertice].pop(self.ListaAdjacencia[vertice].index(verticeRemover))
        
        print(f"Vertice {verticeRemover} exluido com sucesso!\n")

    def RemoverAresta(self, aresta):
        self.ListaAdjacencia[aresta[0]].remove(aresta[1])

        if self.direcional:
            self.ListaAdjacencia[aresta[1]].remove(aresta[0])

        print(f"Aresta {aresta} removida com sucesso!\n")

    def CalcularGrau(self):
        for vertice in self.ListaAdjacencia.keys():
            print(f"Vertice {vertice} tem grau {len(self.ListaAdjacencia[vertice])}\n")
    
    def VerificarAresta(self, vertice1, vertice2):
        if vertice2 in self.ListaAdjacencia[vertice1]:
            print(f"Existe uma aresta {vertice1, vertice2}\n")
        else:
            print(f"Não existe a aresta {vertice1, vertice2}\n")
    
    def ListarVizinhoVertice(self, vertice):
        if vertice in self.ListaAdjacencia:
            print(f"Os vizinhos do vertice {vertice} são: {self.ListaAdjacencia[vertice]}\n")
        else:
            print(f"Não existe o vertice {vertice}")

    def VerificarPercurso(self, percurso):
        for index, vertice in enumerate(percurso):
            if(len(percurso) != index + 1):
                if percurso[index + 1] not in self.ListaAdjacencia[vertice]:
                    print(f"Não tem esse percurso {percurso}\n")
                    return
            else:
                print(f"Tem este percurso {percurso}\n")
                return    

grafo = Grafo("A", False)

grafo.AddVertice("B")
grafo.AddVertice("C")
grafo.AddVertice("D")

grafo.AddAresta("A", "B")
grafo.AddAresta("B", "C")
grafo.AddAresta("C", "D")

grafo.VerificarAresta("C", "D")

grafo.RemoverVertice("D")

grafo.VerificarAresta("C", "D")

grafo.CalcularGrau()

grafo.VerificarAresta("A", "B")
grafo.VerificarAresta("A", "C")

grafo.ListarVizinhoVertice("A")
grafo.ListarVizinhoVertice("B")
grafo.ListarVizinhoVertice("C")

grafo.VerificarPercurso(["A", "B", "C"])
grafo.VerificarPercurso(["A", "C", "B"])

grafo.RemoverAresta(["A", "B"])

grafo.VerificarAresta("A", "B")

grafo.ExibirGrafos()