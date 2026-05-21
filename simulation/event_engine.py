import time

from telemetry.logger import Logger


class EventEngine:
    def __init__(self, network, metrics):
        self.network = network
        self.metrics = metrics

    def transmit_packet(self, packet):
        path = self.network.route_packet(packet)

        Logger.log(f"Routing {packet} via {path}")

        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i + 1]

            node = self.network.nodes[current_node]
            link = node.neighbours[next_node]

            link.add_traffic(packet.size)

            time.sleep(link.latency * 0.2)

            packet.move_to(next_node)

            Logger.log(
                f"Packet {packet.id} moved "
                f"{current_node} -> {next_node}"
            )

        packet.mark_delivered()

        self.metrics.packet_delivered()

        Logger.log(
            f"Packet {packet.id} delivered successfully"
        )