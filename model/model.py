import networkx as nx

from database.DAO import DAO
from model.country import Country


class Model:

    def __init__(self):
        self._grafo=nx.Graph() #ti crei il grafo iniziale
        self._nodes=None #istanza per i nodi
        self._idMap={} #salvi i nodi dentro questo dizionario

    #poi successivamente ti crei il grafo-> ti crei con il DAO i metodi per determinare i nodi e gli archi
    def crea_grafo(self,anno):
        self._nodes=DAO.getAllNodes(anno)
        for e in DAO.getAllNodes(anno):
            self._idMap[e.CCode]=e
        self._grafo.add_nodes_from(self._nodes) #aggiungi i nodi al grafo
        self.addAllEdges(anno) #aggiungi gli archi al grafo

    def addAllEdges(self,anno):
        allEdges=DAO.getAllEdges(anno)
        for e in allEdges:
            c1=self.getCoutry(e.c1)
            c2=self.getCoutry(e.c2)
            self._grafo.add_edge(c1,c2)

    def getNumNodes(self): #returna il num di nodi
        return len(self._grafo.nodes)

    def getNumEdges(self): #returna il numero di archi
        return len(self._grafo.edges)

    def getIdMap(self):
        return self._idMap

    def getCoutry(self,code):
        return self._idMap[code]

    def getNeighbour(self,nodo:Country):
        return len(list(self._grafo.neighbors(nodo))) #GRAFO.neighbour returna un lista dei nodi vicini e returno la sua lunghezza

    def getNumConnected(self):
        return nx.number_connected_components(self._grafo) #mi returna il numero di componenti connesse

    def prova(self):
        for nodo in self._idMap:
            print(self.getCoutry(nodo))

    def statiRaggiungibili(self,stato:Country):
        return list(nx.dfs_tree(self._grafo,stato).nodes) #ricerca bfs o come in questo
        # caso dfs per trovare tutti i nodi raggiungibili a partire da uno