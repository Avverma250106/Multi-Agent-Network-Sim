import json

from core.network import Network
from simulation.traffic_generator import TrafficGenerator
from simulation.event_engine import EventEngine
from telemetry.metrics import Metrics


def build_network(config_path):
    network = Network()

    with open(config_path, "r") as f:
        config = json.load(f)

    for node in config["nodes"]:
        network.add_node(node)

    for link in config["links"]:
        node_a, node_b, bandwidth, latency = link

        network.add_link(
            node_a,
            node_b,
            bandwidth,
            latency
        )

    return network


if __name__ == "__main__":
    network = build_network("configs/topology.json")

    network.display_topology()

    metrics = Metrics()

    traffic_generator = TrafficGenerator(network)

    event_engine = EventEngine(network, metrics)

    print("\n=== Starting Simulation ===\n")

    for _ in range(100):
        packet = traffic_generator.generate_packet()

        metrics.packet_generated()

        event_engine.transmit_packet(packet)
        print()

    for _ in range(100):
        event_engine.process_tick()

    print("=== Simulation Complete ===")

    print(
        f"Delivery Ratio: "
        f"{metrics.delivery_ratio() * 100:.2f}%\n"
        f"Drop Ratio: {metrics.drop_ratio() * 100:.2f}%\n"
        f"Average Queue Delay: {metrics.average_queue_delay():.4f} seconds"
    )