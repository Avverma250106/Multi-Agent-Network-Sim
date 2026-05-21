import networkx as nx


class RoutingEngine:
    def __init__(self, network):
        self.network = network

    def update_graph_weights(self):
        for link in self.network.links:
            self.network.graph[
                link.node_a.node_id
            ][
                link.node_b.node_id
            ][
                "weight"
            ] = link.dynamic_weight()

    def shortest_path(self, source, destination):
        self.update_graph_weights()

        return nx.shortest_path(
            self.network.graph,
            source=source,
            target=destination,
            weight="weight"
        )