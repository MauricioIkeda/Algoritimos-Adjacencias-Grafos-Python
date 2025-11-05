class Grafo:
    def __init__(self, direcional: bool, vertices: list[str]):
        self.direcional = direcional    #Se é direcional ou não
        self.vertices = vertices        #lista de vertices = ["A","B","C","D"]
        self.listaArestas = []          #LISTA DE Arestas = [["A","B"],["B","C"]]

    def existeVertice(self, vertice) -> bool:
        return vertice in self.vertices
    
    def existeAresta(self, vert1, vert2) -> bool: #O verificar Aresta
        return [vert1, vert2] in self.listaArestas or (not self.direcional and [vert2, vert1] in self.listaArestas)
    
    def AddVertice(self, vertice):
        if self.existeVertice(vertice):
            print(f"Já existe a vertice {vertice}")
            return
        self.vertices.append(vertice)
        print(f"Vertice {vertice} adicionada")

    def DelVertice(self, vertice):
        if not self.existeVertice(vertice):
            print(f"Vertice {vertice} não existe")
            return
        self.vertices.remove(vertice)
        print(f'Vertice {vertice} removida')
        arestas_removidas = [a for a in self.listaArestas if vertice in a]
        self.listaArestas = [a for a in self.listaArestas if vertice not in a]
        print(f"Arestas removidas ligadas a {vertice}: {arestas_removidas}")


    def AddAresta(self, vertice1, vertice2):
        if not self.existeVertice(vertice1) or not self.existeVertice(vertice2):
            print(f'Uma das arestas não existe')  #só estou metendo esses comentarios para vc ver no terminal, polui legal
            return
        if self.existeAresta(vertice1, vertice2):
            print(f'Aresta {[vertice1, vertice2]}, já existe')
            return
        self.listaArestas.append([vertice1, vertice2])
        print(f'Aresta {[vertice1, vertice2]} adicionada')
        if not self.direcional:
            self.listaArestas.append([vertice2, vertice1])
            print(f'Aresta {[vertice2, vertice1]} adicionada')

    def DelAresta(self, vert1, vert2):
        if not self.existeAresta(vert1, vert2):
            print(f"Não existe Aresta {[vert1, vert2]}")
            return
        self.listaArestas.remove([vert1, vert2])
        print(f"Aresta {[vert1, vert2]} removida")
        if not self.direcional and [vert2, vert1] in self.listaArestas:
            print(f'Aresta {[vert2, vert1]} removida')
            self.listaArestas.remove([vert2, vert1])

    def CalcularGrauDeUm(self, vert):
        if not self.existeVertice(vert):
            return
        if self.direcional:
            grauEntrada = sum(1 for a in self.listaArestas if a[1] == vert)
            grauSaida = sum(1 for a in self.listaArestas if a[0] == vert)
            print(f'{vert} -> Grau de entrada: {grauEntrada}, Grau de saída: {grauSaida}')
        else:
            grau = sum(1 for a in self.listaArestas if a[0] == vert)
            print(f'{vert} -> Grau: {grau}')

    def CalculaGrauGeral(self):
        print('\n')
        for vertice in self.vertices:
            self.CalcularGrauDeUm(vertice)
        print('\n')
        return

    def VerificarVizinho(self, vert):
        if not self.existeVertice(vert):
            return
        vizinhos = [a[1] for a in self.listaArestas if a[0] == vert]
        print(f'{vert}: {" ".join(vizinhos) if vizinhos else "(sem vizinhos)"}')

    def VerificarPercurso(self, percurso: list[str]):
        for i in range(len(percurso) - 1):
            v1, v2 = percurso[i], percurso[i + 1]
            if not self.existeVertice(v1) or not self.existeVertice(v2) or not self.existeAresta(v1, v2):
                print(f'Percurso inválido: não há aresta entre {v1} e {v2}')
                return False
        print(f'Percurso {" -> ".join(percurso)} é válido')
        return True
    
    def ExibirGrafo(self):
        self.listaArestas.sort()
        print("\nGrafinho:")
        for aresta in self.listaArestas:
            print(f"{aresta[0]} : {aresta[1]}")

g = Grafo(False, ["A", "B", "C", "D"])
g.AddVertice("A")
g.AddVertice("E")
g.AddAresta("A", "B")
g.AddAresta("B", "C")
g.AddAresta("C", "D")
g.AddAresta("A", "E")

g.CalculaGrauGeral()
g.CalcularGrauDeUm("A")

g.VerificarPercurso(["A", "B", "C"])
g.VerificarPercurso(["A", "C"])

g.DelVertice("D")

g.ExibirGrafo()
