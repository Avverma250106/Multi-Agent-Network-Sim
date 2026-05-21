class Node:
    def __init__(self,node_id):
        self.node_id = node_id
        self.neighbours = {}
        self.queue = []

        self.received_packets = 0
        self.send_packets = 0

    def add_neighbours(self,neighbour,link):
        self.neighbours[neighbour] = link 

    def rcv_pkt(self,packet):
        self.queue.append(packet)
        # self.received_packets.append(packet)
        self.received_packets += 1

    def send_packet(self):
        if not self.queue:
            return None

        self.sent_packets += 1
        return self.queue.pop(0)

    def __repr__(self):
        return f"Node({self.node_id})"