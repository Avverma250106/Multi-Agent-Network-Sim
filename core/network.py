import networkx as nx

from core.node import Node
from core.link import Link
from core.routing import RoutingEngine


class Network:
    def __init__(self):
        self.nodes = {}
        self.links = []

        self.graph = nx.Graph()

        self.routing_engine = RoutingEngine(self)

    def add_node(self, node_id):
        node = Node(node_id)

        self.nodes[node_id] = node
        self.graph.add_node(node_id)

    def add_link(self, node_a, node_b, bandwidth=100, latency=1):
        node1 = self.nodes[node_a]
        node2 = self.nodes[node_b]

        link = Link(node1, node2, bandwidth, latency)

        node1.add_neighbours(node2.node_id, link)
        node2.add_neighbours(node1.node_id, link)

        self.links.append(link)

        self.graph.add_edge(
            node_a,
            node_b,
            weight=latency
        )

    def route_packet(self, packet):
        path = self.routing_engine.shortest_path(
            packet.current_node,
            packet.destination
        )

        return path

    def display_topology(self):
        print("\n=== Network Topology ===")

        for link in self.links:
            print(link)