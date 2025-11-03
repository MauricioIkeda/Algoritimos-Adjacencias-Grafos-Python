class Grafo:
    def __init__(self, direcional: bool, vertices: list[str]):
        self.direcional = direcional
        self.vertices = vertices                  # Lista de vértices
        self.listaArestas = []                    # Lista de arestas (ex: [['A','B'], ['B','C']])


    def AddVertice(self, vertice):
        if vertice in self.vertices:
            print(f'{vertice} já existe no grafo')
        else:
            self.vertices.append(vertice)
            print(f'{vertice} adicionado ao grafo')

    def DelVertice(self, vertice):
        if vertice not in self.vertices:
            print(f'{vertice} não existe no grafo')
            return
        self.vertices.remove(vertice)

        self.listaArestas = [a for a in self.listaArestas if vertice not in a]
        print(f'{vertice} e suas arestas foram removidos')

    def AddAresta(self, vertice1, vertice2):
        if vertice1 not in self.vertices or vertice2 not in self.vertices:
            print(f'{vertice1} ou {vertice2} não existem no grafo')
            return

        if [vertice1, vertice2] in self.listaArestas:
            print(f'Aresta {vertice1}-{vertice2} já existe')
            return

        self.listaArestas.append([vertice1, vertice2])
        if not self.direcional:
            self.listaArestas.append([vertice2, vertice1])
        print(f'Aresta {vertice1}-{vertice2} adicionada')

    def DelAresta(self, vert1, vert2):
        if [vert1, vert2] not in self.listaArestas:
            print(f'Aresta {vert1}-{vert2} não existe')
            return

        self.listaArestas.remove([vert1, vert2])
        if not self.direcional and [vert2, vert1] in self.listaArestas:
            self.listaArestas.remove([vert2, vert1])
        print(f'Aresta {vert1}-{vert2} removida')

    def CalcularGrau(self, vert):
        if vert not in self.vertices:
            print(f'{vert} não existe no grafo')
            return

        if self.direcional:
            grauEntrada = sum(1 for a in self.listaArestas if a[1] == vert)
            grauSaida = sum(1 for a in self.listaArestas if a[0] == vert)
            print(f'{vert} -> Grau de entrada: {grauEntrada}, Grau de saída: {grauSaida}')
        else:
            grau = sum(1 for a in self.listaArestas if a[0] == vert)
            print(f'{vert} -> Grau: {grau}')

    def VerificarAresta(self, vert1, vert2):
        if vert1 not in self.vertices or vert2 not in self.vertices:
            print('Algum dos vértices não existe no grafo')
            return

        if [vert1, vert2] in self.listaArestas:
            print(f'Existe aresta de {vert1} para {vert2}')
        else:
            print(f'Não existe aresta de {vert1} para {vert2}')


    def VerificarVizinho(self, vert):
        if vert not in self.vertices:
            print(f'{vert} não existe no grafo')
            return

        vizinhos = [a[1] for a in self.listaArestas if a[0] == vert]
        print(f'{vert}: {" ".join(vizinhos) if vizinhos else "(sem vizinhos)"}')

    def VerificarPercurso(self, percurso: list[str]):
        for i in range(len(percurso) - 1):
            v1, v2 = percurso[i], percurso[i + 1]
            if [v1, v2] not in self.listaArestas:
                print(f'Percurso inválido: não há aresta entre {v1} e {v2}')
                return False
        print(f'Percurso {" -> ".join(percurso)} é válido')
        return True
    
g = Grafo(False, ["A", "B", "C", "D"])
g.AddAresta("A", "B")
g.AddAresta("B", "C")
g.AddAresta("C", "D")
g.AddAresta('A','E')

g.VerificarPercurso(["A", "B", "C"]) 
g.VerificarPercurso(["A", "C"])
