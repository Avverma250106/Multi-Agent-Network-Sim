import uuid 
import time

class Packet:
    def __init__(self,source,destination,size=1):
        self.id = str(uuid.uuid4())[:8]
        self.source = source
        self.destination = destination
        self.size = size 

        self.created_at = time.time()
        self.current_node = source 

        self.path = [source]
        self.delivered = False

    def move_to(self,node):
        self.current_node = node
        self.path.append(node)

    def mark_delivered(self):
        self.delivered = True

    def __repr__(self):
        return f"Packet({self.id}, {self.source} -> {self.destination}, size={self.size})"