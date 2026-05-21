class Link:
    def __init__(
        self,
        node_a,
        node_b,
        bandwidth=100,
        latency=1,
        max_queue_size=10
    ):
        self.node_a = node_a
        self.node_b = node_b

        self.bandwidth = bandwidth
        self.latency = latency

        self.current_load = 0

        self.max_queue_size = max_queue_size

        self.dropped_packets = 0

    def get_other_node(self, node):
        if node == self.node_a:
            return self.node_b

        return self.node_a

    def add_traffic(self, amount=1):
        self.current_load += amount

    def clear_traffic(self):
        self.current_load = 0

    def utilization(self):
        return self.current_load / self.bandwidth

    def is_congested(self):
        return self.current_load >= self.max_queue_size

    def drop_packet(self):
        self.dropped_packets += 1

    def dynamic_weight(self):
        congestion_penalty = self.utilization() * 10

        return self.latency + congestion_penalty

    def __repr__(self):
        return (
            f"Link({self.node_a.node_id} <-> "
            f"{self.node_b.node_id}, "
            f"load={self.current_load}, "
            f"util={self.utilization():.2f})"
        )