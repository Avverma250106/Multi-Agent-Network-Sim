class Link:
    def __init__(self,node_a,node_b,bandwidth=100,latency=1):
        self.node_a = node_a
        self.node_b = node_b
        self.bandwidth = bandwidth
        self.latency = latency

        self.current_load = 0

    def get_other_node(self,node):
        if node == self.node_a:
            return self.node_b
        return self.node_a
    
    def add_traffic(self,amount=1):
        self.current_load += amount

    def clear_traffic(self):
        self.current_load = 0

    def utilisation(self):
        return self.current_load / self.bandwidth
    
    def __repr__(self):
        return f"Link({self.node_a.node_id} <-> {self.node_b.node_id}, bw={self.bandwidth}, lat={self.latency})"
    
