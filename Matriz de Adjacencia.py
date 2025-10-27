class Grafo():
    def __init__(self):
        self.MatrizAdjacencia = []
        self.ListaVertices = []
        self.debugar = True
    
    def ExibirMatriz(self):
        largura_coluna = max([len(v) for v in self.ListaVertices] + [3])

        print(" " * (largura_coluna + 3), end="")
        for nome in self.ListaVertices:
            print(f"{nome:>{largura_coluna}}", end=" ")
        print()

        for index, linha in enumerate(self.MatrizAdjacencia):
            print(f"{self.ListaVertices[index]:<{largura_coluna}} |", end=" ")
            for elemento in linha:
                print(f"{elemento:>{largura_coluna}}", end=" ")
            print()
        print()

    def AddVertice(self, nomeVertice):
        verticeNovo = [[], nomeVertice]

        self.MatrizAdjacencia.append(verticeNovo[0])
        self.ListaVertices.append(verticeNovo[1])
        for coluna in self.MatrizAdjacencia:
            while len(coluna) != len(self.MatrizAdjacencia):
                coluna.append(0)
        
        print("Vertice adicionado com sucesso!")
        self.ExibirMatriz()
    
    def AddAresta(self, vertice1Nome, vertice2Nome):
        index1 = self.ListaVertices.index(vertice1Nome)
        index2 = self.ListaVertices.index(vertice2Nome)

        self.MatrizAdjacencia[index1][index2] = 1

        print(f"Aresta adicionado com sucesso na linha {vertice1Nome} no coluna {vertice2Nome}")
        self.ExibirMatriz()

    def RemoverVertice(self, verticeNome):
        indiceVertice = self.ListaVertices.index(verticeNome)
        self.ListaVertices.pop(indiceVertice)
        self.MatrizAdjacencia.pop(indiceVertice)

        for coluna in self.MatrizAdjacencia:
            coluna.pop(indiceVertice)

        print(f"Vertice {verticeNome} exluido com sucesso!\n")
        self.ExibirMatriz()

    def RemoverAresta(self, vertice1Nome, vertice2Nome):
        index1 = self.ListaVertices.index(vertice1Nome)
        index2 = self.ListaVertices.index(vertice2Nome)
        self.MatrizAdjacencia[index1][index2] = 0

        print(f"Aresta do vertice ({vertice1Nome}, {vertice2Nome}) removida com sucesso!\n")
        self.ExibirMatriz()

    def CalcularGrauEntrada(self):
        print("=================================")
        for index in range(len(self.MatrizAdjacencia)):
            grauEntrada = 0
            for coluna in self.MatrizAdjacencia:
                grauEntrada += coluna[index]
            print(f"O grau de entrada do vertice {index + 1} é {grauEntrada}")
        print("=================================\n")

    def CalcularGrauSaida(self):
        print("=================================")
        for index, coluna in enumerate(self.MatrizAdjacencia):
            grauEntrada = sum(coluna)
            print(f"O grau de saida do vertice {index + 1} é {grauEntrada}")
        print("=================================\n")
    
    def VerificarAresta(self, vertice1Nome, vertice2Nome):
        index1 = self.ListaVertices.index(vertice1Nome)
        index2 = self.ListaVertices.index(vertice2Nome)
        teste = self.MatrizAdjacencia[index1][index2]

        if teste == 1:
            print(f"Existe uma aresta {vertice1Nome, vertice2Nome}\n")
        else:
            print(f"Não existe a aresta {vertice1Nome, vertice2Nome}\n")
    
    def ListarVizinhoVertice(self, verticeNome):
        vizinhos = set()

        vertice = self.ListaVertices.index(verticeNome)

        for indexColuna, valor in enumerate(self.MatrizAdjacencia[vertice]):
            if valor == 1:
                vizinhos.add(self.ListaVertices[indexColuna])

        for indexLinha, linha in enumerate(self.MatrizAdjacencia):
            if linha[vertice - 1] == 1:
                vizinhos.add(self.ListaVertices[indexLinha])
        
        if self.debugar == True:
            print(f"Os vizinhos do vértice {verticeNome} são {sorted(vizinhos)}\n")
        return vizinhos


    def VerificarPercurso(self, percurso):
        self.debugar = False

        percursoVerificar = percurso.copy()
        percursoVerificar.pop()

        for vertice in percursoVerificar:
            if vertice not in self.ListarVizinhoVertice(vertice):
                print(f"Não existe este percurso {percurso}")
                return

        print(f"Existe o percurso {percurso}")
        self.debugar = True


grafo = Grafo()

grafo.AddVertice("V1")
grafo.AddVertice("V2")
grafo.AddVertice("V3")
grafo.AddVertice("V4")

grafo.AddAresta("V1", "V1")
grafo.AddAresta("V1", "V3")
grafo.AddAresta("V3", "V2")
grafo.AddAresta("V2", "V3")
grafo.AddAresta("V3", "V4")
grafo.AddAresta("V3", "V1")

grafo.RemoverAresta("V2", "V3")

grafo.CalcularGrauEntrada()
grafo.CalcularGrauSaida()

grafo.VerificarAresta("V1", "V3")
grafo.VerificarAresta("V2", "V1")

grafo.ListarVizinhoVertice("V1")

grafo.ExibirMatriz()
grafo.VerificarPercurso(["V2", "V1", "V3"])
grafo.VerificarPercurso(["V1", "V3", "V4"])

grafo.RemoverVertice("V2")