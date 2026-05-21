import random

from core.packet import Packet


class TrafficGenerator:
    def __init__(self, network):
        self.network = network

    def generate_packet(self):
        nodes = list(self.network.nodes.keys())

        source = random.choice(nodes)
        destination = random.choice(nodes)

        while destination == source:
            destination = random.choice(nodes)

        return Packet(source, destination)