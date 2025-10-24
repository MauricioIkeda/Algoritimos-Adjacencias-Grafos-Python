class Grafo():
    def __init__(self):
        self.MatrizAdjacencia = []
        self.debugar = True
    
    def ExibirMatriz(self):
        for linha in self.MatrizAdjacencia:
            for elemento in linha:
                print(elemento, end=" ")
            print()
        print()

    def AddVertice(self):
        verticeNovo = []

        self.MatrizAdjacencia.append(verticeNovo)
        for coluna in self.MatrizAdjacencia:
            while len(coluna) != len(self.MatrizAdjacencia):
                coluna.append(0)
        
        print("Vertice adicionado com sucesso!")
        self.ExibirMatriz()
    
    def AddAresta(self, vertice1, vertice2):
        self.MatrizAdjacencia[vertice1- 1][vertice2- 1] = 1

        print(f"Aresta adicionado com sucesso na linha {vertice1} no coluna {vertice2}")
        self.ExibirMatriz()

    def RemoverVertice(self, verticeNumero):
        self.MatrizAdjacencia.pop(verticeNumero- 1)
        for coluna in self.MatrizAdjacencia:
            coluna.pop(verticeNumero- 1)

        print(f"Vertice {verticeNumero} exluido com sucesso! Vertice {verticeNumero + 1} virou o novo vertice {verticeNumero}\n")
        self.ExibirMatriz()

    def RemoverAresta(self, vertice1, vertice2):
        self.MatrizAdjacencia[vertice1- 1][vertice2 - 1] = 0

        print(f"Aresta do vertice ({vertice1 - 1}, {vertice2 -1}) removida com sucesso!\n")
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
    
    def VerificarAresta(self, vertice1, vertice2):
        teste = self.MatrizAdjacencia[vertice1 - 1][vertice2 - 1]

        if teste == 1:
            print(f"Existe uma aresta {vertice1, vertice2}\n")
        else:
            print(f"Não existe a aresta {vertice1, vertice2}\n")
    
    def ListarVizinhoVertice(self, vertice):
        vizinhos = set()

        for indexColuna, valor in enumerate(self.MatrizAdjacencia[vertice - 1]):
            if valor == 1:
                vizinhos.add(indexColuna + 1)

        for indexLinha, linha in enumerate(self.MatrizAdjacencia):
            if linha[vertice - 1] == 1:
                vizinhos.add(indexLinha + 1)
        
        if self.debugar == True:
            print(f"Os vizinhos do vértice {vertice} são {sorted(vizinhos)}\n")
        return vizinhos


    def VerificarPercurso(self, percurso):
        self.debugar = False

        for index, vertice in enumerate(percurso):
            if index + 1 <= len(percurso) - 1 and percurso[index + 1] not in self.ListarVizinhoVertice(vertice):
                print(f"Não existe este percurso {percurso}")
                return

        print(f"Existe o percurso {percurso}")
        self.debugar = True


grafo = Grafo()

grafo.AddVertice()
grafo.AddVertice()
grafo.AddVertice()
grafo.AddVertice()

grafo.AddAresta(1, 1)
grafo.AddAresta(1, 3)
grafo.AddAresta(3, 2)
grafo.AddAresta(2, 3)
grafo.AddAresta(3, 4)
grafo.AddAresta(3, 1)

grafo.RemoverAresta(2, 3)

grafo.CalcularGrauEntrada()
grafo.CalcularGrauSaida()

grafo.VerificarAresta(1, 3)
grafo.VerificarAresta(2, 1)

grafo.ListarVizinhoVertice(2)

grafo.VerificarPercurso([2, 1, 3])
grafo.VerificarPercurso([1, 3, 4])

grafo.RemoverVertice(2)