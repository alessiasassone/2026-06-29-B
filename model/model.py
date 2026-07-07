import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}
        self._nodes = []

    def getAllNodes(self):
        return DAO.getAllNodes()

    def buildGraph(self):
        self._graph.clear()

        self._nodes = DAO.getAllNodes()
        for n in self._nodes:
            self._idMap[n.AlbumId] = n

        self._graph.add_nodes_from(self._nodes)

        allEdges = DAO.getAllEdges(self._idMap)
        for e in allEdges:
            self._graph.add_edge(e.n1, e.n2)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getConnessaInfo(self):
        components = list(nx.connected_components(self._graph))
        largest = max(components, key=len)

        subgraph = self._graph.subgraph(largest).copy()
        orderedNodes = sorted(subgraph.nodes(), key=lambda n: n.Title.lower())

        details = [(n.Title, n.NumBrani) for n in orderedNodes]

        return len(components), largest, details