import time

from core import link, packet
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

            if link.is_congested():
                link.drop_packet()
                self.metrics.packet_dropped()

                Logger.log(
                    f"Packet {packet.id} DROPPED due to congestion "
                    f"on {current_node} -> {next_node}"
                )
                self.network.decay_network_traffic()
                return

            success = link.enqueue_packet(packet)
            if not success:
                self.metrics.packet_dropped()

                Logger.log(
                    f"Packet {packet.id} DROPPED due to full queue "
                    f"on {current_node} -> {next_node}"
                )

                self.network.decay_network_traffic()    

                return
            
            Logger.log(
                f"Packet {packet.id} queued on "
                f"{current_node} -> {next_node}"
            )

            time.sleep(link.latency * 0.2)

            transmitted_packet = link.dequeue_packet()

            if transmitted_packet:
                self.metrics.add_queue_delay(
                transmitted_packet.queue_delay()
            )
                
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

        self.network.network_decay_traffic()