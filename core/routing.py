import networkx as nx

class RoutingEngine:
    def __init__(self,network):
        self.network = network

    def shortest_path(self, source, destination):
        graph = self.network.graph

        return nx.shortest_path(
            graph,
            source=source,
            target=destination,
            weight="weight"
        )