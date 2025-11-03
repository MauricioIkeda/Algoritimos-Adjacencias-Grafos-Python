# 🧮 Grafos em Python — Matriz e Lista de Adjacência

Este repositório contém duas implementações em Python para representar **grafos não direcionados e direcionados**, utilizando as estruturas de **Lista de Adjacência** e **Matriz de Adjacência** respectivamente.
Esses algoritmos são ótimos para fins didáticos e podem ser adaptados para aplicações mais complexas de **Teoria dos Grafos** e **Estruturas de Dados**.

---

## 👤 Autores

Nome: Mauricio Shiguemitsu Kamado Ikeda // RA: 1999029
Nome: Vinicius Estevão Consolino Brandi // RA: 2002558
Nome: Vitor Soares Dos Santos // RA : 2002898


---

## 📂 Estrutura do Projeto

```
📦 Grafos
 ┣ 📜 Lista de Adjacencia.py
 ┗ 📜 Matriz de Adjacencia.py
```

Cada arquivo implementa a classe `Grafo` de forma independente, com métodos próprios para manipular vértices e arestas, além de realizar operações típicas de análise de grafos.

---

## 🧩 Representações de Grafos

### 🔹 Lista de Adjacência

**Arquivo:** `Lista de Adjacencia.py`

Representa o grafo com um **dicionário**, onde cada vértice é uma chave, e o valor é uma **lista com seus vizinhos**.
Essa abordagem é mais eficiente em **grafos esparsos**, onde há poucas conexões entre os vértices.

#### 🔧 Métodos disponíveis:

| Método                        | Descrição                                              |
| ----------------------------- | ------------------------------------------------------ |
| `AddVertice(vertice)`         | Adiciona um novo vértice ao grafo.                     |
| `AddAresta(v1, v2)`           | Cria uma conexão bidirecional entre dois vértices.     |
| `RemoverVertice(v)`           | Remove um vértice e todas as arestas ligadas a ele.    |
| `RemoverAresta([v1, v2])`     | Remove a aresta entre dois vértices.                   |
| `CalcularGrau()`              | Exibe o grau (quantidade de conexões) de cada vértice. |
| `VerificarAresta(v1, v2)`     | Verifica se existe uma aresta entre os vértices.       |
| `ListarVizinhoVertice(v)`     | Mostra os vizinhos diretos de um vértice.              |
| `VerificarPercurso(percurso)` | Verifica se um percurso informado é válido.            |

#### 🧠 Exemplo de uso:

```python
grafo = Grafo("A")

grafo.AddVertice("B")
grafo.AddVertice("C")
grafo.AddAresta("A", "B")
grafo.AddAresta("B", "C")

grafo.ListarVizinhoVertice("B")
grafo.VerificarPercurso(["A", "B", "C"])
```

#### 🖥️ Exemplos de saída:

```
Os vizinhos do vertice B são: ['A', 'C']
Tem este percurso ['A', 'B', 'C']
```

---

### 🔹 Matriz de Adjacência

**Arquivo:** `Matriz de Adjacencia.py`

Representa o grafo através de uma **matriz quadrada**, onde cada linha e coluna correspondem a um vértice.
Um valor `1` na posição `[i][j]` indica a existência de uma aresta entre os vértices `i` e `j`.

#### 🔧 Métodos disponíveis:

| Método                        | Descrição                                            |
| ----------------------------- | ---------------------------------------------------- |
| `AddVertice()`                | Adiciona um novo vértice à matriz.                   |
| `AddAresta(v1, v2)`           | Cria uma conexão entre dois vértices.                |
| `RemoverVertice(v)`           | Remove um vértice da matriz.                         |
| `RemoverAresta(v1, v2)`       | Remove a aresta entre dois vértices.                 |
| `CalcularGrauEntrada()`       | Calcula o grau de entrada de cada vértice.           |
| `CalcularGrauSaida()`         | Calcula o grau de saída de cada vértice.             |
| `VerificarAresta(v1, v2)`     | Verifica se há uma aresta entre dois vértices.       |
| `ListarVizinhoVertice(v)`     | Lista os vértices vizinhos de um vértice específico. |
| `VerificarPercurso(percurso)` | Verifica se um percurso informado é válido.          |

#### 🧠 Exemplo de uso:

```python
grafo = Grafo()

grafo.AddVertice()
grafo.AddVertice()
grafo.AddVertice()

grafo.AddAresta(1, 3)
grafo.AddAresta(2, 1)
grafo.AddAresta(3, 2)

grafo.ExibirMatriz()
grafo.CalcularGrauSaida()
```

#### 🖥️ Exemplos de saída:

Ao adicionar os vértices, a matriz cresce automaticamente:

```
Vertice adicionado com sucesso!
0
Vertice adicionado com sucesso!
0 0
0 0
Vertice adicionado com sucesso!
0 0 0
0 0 0
0 0 0
```

Depois de adicionar algumas arestas:

```
Aresta adicionado com sucesso na linha 1 no coluna 3
0 0 1
0 0 0
0 0 0

Aresta adicionado com sucesso na linha 2 no coluna 1
0 0 1
1 0 0
0 0 0

Aresta adicionado com sucesso na linha 3 no coluna 2
0 0 1
1 0 0
0 1 0
```

Ao calcular o grau de saída:

```
=================================
O grau de saida do vertice 1 é 1
O grau de saida do vertice 2 é 1
O grau de saida do vertice 3 é 1
=================================
```

---

## ⚙️ Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/SEU_USUARIO/grafos-python.git
   ```
2. Entre na pasta:

   ```bash
   cd grafos-python
   ```
3. Execute um dos arquivos:

   ```bash
   python "Lista de Adjacencia.py"
   ```

   ou

   ```bash
   python "Matriz de Adjacencia.py"
   ```

Os scripts já contêm **exemplos práticos de execução**, então você verá os resultados diretamente no terminal.

---

## 🧠 Conceitos Envolvidos

* Representações de Grafos (Matriz vs Lista de Adjacência)
* Grau de entrada e saída
* Verificação de arestas e percursos
* Manipulação dinâmica de vértices e conexões

---

## 📘 Projeto acadêmico desenvolvido em Python para estudo de representações e manipulação de grafos.

Se este projeto te ajudou, ⭐ **considere deixar uma estrela no repositório!**
