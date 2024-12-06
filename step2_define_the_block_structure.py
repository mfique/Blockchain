import hashlib

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index 
        self.timestamp = timestamp 
        self.data = data 
        self.previous_hash = previous_hash  
        self.proof = 0 
        self.hash = self.compute_hash()

    def compute_hash(self):
     
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.proof}"
        return hashlib.sha256(block_string.encode()).hexdigest()
