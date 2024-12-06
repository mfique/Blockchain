import hashlib
import time
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        """
        Initialize a new block in the blockchain
        
        :param index: Unique block number
        :param timestamp: Time of block creation
        :param data: Transaction or block data
        :param previous_hash: Hash of the previous block in the chain
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # Used for Proof of Work
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """
        Calculate SHA-256 hash of the block
        
        :return: Calculated hash string
        """
        # Convert block data to a string for hashing
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty):
        """
        Implement Proof of Work mining
        
        :param difficulty: Number of leading zeros required in hash
        """
        target = '0' * difficulty
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self, difficulty=4):
        """
        Initialize the blockchain with a genesis block
        
        :param difficulty: Mining difficulty for Proof of Work
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
    
    def create_genesis_block(self):
        """
        Create the first block in the blockchain
        
        :return: Genesis block
        """
        return Block(0, time.time(), "Genesis Block", "0")
    
    def get_latest_block(self):
        """
        Get the most recently added block
        
        :return: Last block in the chain
        """
        return self.chain[-1]
    
    def add_block(self, new_block):
        """
        Add a new block to the blockchain
        
        :param new_block: Block to be added
        """
        new_block.previous_hash = self.get_latest_block().hash
        
        
        new_block.mine_block(self.difficulty)
        
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        """
        Validate the entire blockchain
        
        :return: Boolean indicating blockchain integrity
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True

def main():
    my_blockchain = Blockchain(difficulty=4)
    
    print("Mining block 1...")
    my_blockchain.add_block(Block(1, time.time(), {"amount": 10}))
    
    print("Mining block 2...")
    my_blockchain.add_block(Block(2, time.time(), {"amount": 20}))
    
    print(f"Is blockchain valid? {my_blockchain.is_chain_valid()}")
    
    for block in my_blockchain.chain:
        print(f"Block #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print("---")

if __name__ == "__main__":
    main()