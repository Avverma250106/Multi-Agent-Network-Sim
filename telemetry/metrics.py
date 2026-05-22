class Metrics:
    def __init__(self):
        self.total_packets = 0
        self.delivered_packets = 0
        self.dropped_packets = 0
        self.total_queue_delay = 0

    def packet_generated(self):
        self.total_packets += 1

    def packet_delivered(self):
        self.delivered_packets += 1

    def packet_dropped(self):
        self.dropped_packets += 1

    def add_queue_delay(self, delay):
        self.total_queue_delay += delay

    def delivery_ratio(self):
        if self.total_packets == 0:
            return 0

        return self.delivered_packets / self.total_packets

    def drop_ratio(self):
        if self.total_packets == 0:
            return 0
        
        return self.dropped_packets / self.total_packets
        
    def average_queue_delay(self):
        if self.delivered_packets == 0:
            return 0
        
        return (
        self.total_queue_delay
        / self.delivered_packets
        )
