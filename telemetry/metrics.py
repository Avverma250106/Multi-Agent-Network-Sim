class Metrics:
    def __init__(self):
        self.total_packets = 0
        self.delivered_packets = 0

    def packet_generated(self):
        self.total_packets += 1

    def packet_delivered(self):
        self.delivered_packets += 1

    def delivery_ratio(self):
        if self.total_packets == 0:
            return 0

        return self.delivered_packets / self.total_packets