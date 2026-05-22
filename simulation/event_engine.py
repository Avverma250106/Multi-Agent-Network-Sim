import time

from core import link, packet
from telemetry.logger import Logger


class EventEngine:
    def __init__(self, network, metrics):
        self.network = network
        self.metrics = metrics
        self.active_packets = []
        self.pending_transmissions = []

    def transmit_packet(self, packet):
        path = self.network.route_packet(packet)
        self.active_packets.append(
            {
                "packet": packet,
                "path": path,
                "current_hop": 0
            }
        )

        Logger.log(
            f"Registered Packet {packet.id} "
            f"for simulation"
        )

    def process_tick(self):
        Logger.log("=== Processing Tick ===")

        completed_packets = []

        for packet_state in self.active_packets:
            packet = packet_state["packet"]

            path = packet_state["path"]

            current_hop = packet_state["current_hop"]

            if current_hop >= len(path) - 1:
                packet.mark_delivered()

                self.metrics.packet_delivered()

                Logger.log(
                    f"Packet {packet.id} delivered"
                )

                completed_packets.append(packet_state)

                continue

            current_node = path[current_hop]

            next_node = path[current_hop + 1]

            node = self.network.nodes[current_node]

            link = node.neighbours[next_node]

            success = link.enqueue_packet(packet)

            self.pending_transmissions.append({
                "packet-state": packet_state,
                "link" : link,
                "next_node" : next_node,
                "current_node" : current_node
                }
            )

            if not success:
                self.metrics.packet_dropped()

                Logger.log(
                    f"Packet {packet.id} dropped "
                    f"on {current_node} -> {next_node}"
                )

                completed_packets.append(packet_state)

                continue

            

        for completed in completed_packets:
            self.active_packets.remove(completed)

        processed_transmissions = []

        for transmission in self.pending_transmissions:
            packet_state = transmission["packet-state"]
            link = transmission["link"]
            next_node = transmission["next_node"]
            current_node = transmission["current_node"]
            processed_packets = link.process_queue()

            for processed_packet in processed_packets:
                processed_packet.move_to(next_node)

                packet_state["current_hop"] += 1

                self.metrics.add_queue_delay(
                    processed_packet.queue_delay()
                )

                Logger.log(
                    f"Packet {processed_packet.id} "
                    f"moved {current_node} -> {next_node}"
                )

                processed_transmissions.append(
                    transmission
                )

        for processed in processed_transmissions:
            if processed in self.pending_transmissions:
                self.pending_transmissions.remove(processed)


        self.network.network_decay_traffic()