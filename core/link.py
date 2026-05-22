import time 
from collections import deque

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
        self.packet_queue = deque()

        self.dropped_packets = 0
        self.transmitted_packets = 0

        self.last_decay_time = time.time()
        self.decay_factor = 0.5

    def get_other_node(self, node):
        if node == self.node_a:
            return self.node_b

        return self.node_a

    def add_traffic(self, amount=1):
        self.current_load += amount

    def enqueue_packet(self,packet):
        if len(self.packet_queue) >= self.max_queue_size:
            self.drop_packet()
            return False
        
        packet.queue_entry_time = time.time()
        self.packet_queue.append(packet)
        self.current_load += packet.size
        return True
    
    def dequeue_packet(self):
        if not self.packet_queue:
            return None
        
        packet = self.packet_queue.popleft()
        packet.queue_exit_time = time.time()
        self.current_load = max(0, self.current_load - packet.size)
        self.transmitted_packets += 1
        return packet

    def clear_traffic(self):
        self.current_load = 0

    def utilization(self):
        return self.current_load / self.bandwidth
    
    def queue_length(self):
        return len(self.packet_queue)

    def is_congested(self):
        return len(self.packet_queue) >= self.max_queue_size

    def drop_packet(self):
        self.dropped_packets += 1

    def dynamic_weight(self):
        congestion_penalty = self.utilization()*10
        queue_penalty = self.queue_length()*2
        return self.latency + congestion_penalty + queue_penalty
    
    def decay_traffic(self):
        now = time.time()
        elapsed = now - self.last_decay_time    
        decay_amount = elapsed*self.decay_factor*self.bandwidth
        self.current_load = max(0, self.current_load - decay_amount)
        self.last_decay_time = now

    def __repr__(self):
        return (
            f"Link({self.node_a.node_id} <-> "
            f"{self.node_b.node_id}, "
            f"load={self.current_load}, "
            f"util={self.utilization():.2f})"
        )