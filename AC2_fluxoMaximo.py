"""
* Edgar Rosotti Navarro 180669
* Eduardo Campos Gonçalves 190309
* Gabriel Maciel Silvério 190654
* João Victor da Costa Wudarski 190823
* Johanna Bernecker 190737
* Matheus Bernardo Frate 190110
* Vitor Guilherme Sanches Magnani de Sobral 190093
"""
# CLASSE GRAFO
class Graph:

    # CONSTRUTOR DO GRAFO
    def __init__(self):
        self.graph = graph
        self.ROW = len(graph)
        
    # METODO PARA ENCONTRAR O CAMINHO
    def bfs(self, s, t, parent):
        # MARCA LISTA DE VISITADOS COMO VAZIA
        visited = [False] * (self.ROW)
        queue = []
        
        # ADICIONA O SOURCE NA PRIMEIRA POSIÇÃO DA QUEUE
        queue.append(s)
        
        # MARCA O SOURCE COMO VERTICE VISITADO
        visited[s] = True
        
        while queue:
            
            u = queue.pop(0)
            
            for ind, val in enumerate(self.graph[u]):
                
                # SE O VERTICE ATUAL NÃO TIVER SIDO VISITADO E O VALOR FOR MAIOR QUE ZERO, OU SEJA A CAPACIDADE MÁXIMA DA ARESTA NÃO FOI ATINGIDA
                if visited[ind] is False and val > 0:
                    
                    # ADICIONA O VERTICE NA QUEUE
                    queue.append(ind)
                    
                    # COLOCA O VERTICE NA LISTA DE VISITADOS
                    visited[ind] = True
                    parent[ind] = u
                    
                    # SE O VERTICE ATUAL FOR O RALO, ELE SAI DO BFS E RETORNA PARA O FORD-FUNLKERSON O CAMINHO ENCONTRADO
                    if visited[ind] == visited[t]:
                        return True
        return False
    
    # ALGORITIMO FORD-FUNLKERSON
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        
        # ENQUANTO O BFS ESTIVER ENCOTRANDO UM CAMINHO, O FLUXO MÁXIMO DE CADA CAMINHO É SOMADO AO FLUXO TOTAL
        while self.bfs(source, sink, parent):
            
            path_flow = float("inf")
            s = sink
    
            while(s != source):
            
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            
            max_flow += path_flow
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        
        # QUANDO O BFS NÃO ENCONTRA MAIS UM CAMINHO, OU SEJA RETORNA FALSE, O FLUXO É MÁXIMO 
        return max_flow

graph =  [[0, 15, 4, 0, 0, 0],
         [0, 0, 0, 12, 0, 0],
         [0, 0, 0, 0, 10, 0],
         [0, 0, 3, 0, 0, 7],
         [0, 5, 0, 0, 0, 10],
         [0, 0, 0, 0, 0, 0]]

g = Graph()

source = 0
sink = 5

print("Max Flow : %d " % g.ford_fulkerson(source, sink))
