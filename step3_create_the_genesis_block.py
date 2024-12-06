from step2_define_the_block_structure import Block
import datetime

class Blockchain:
    def __init__(self):
     
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2 

    def create_genesis_block(self):
  
        return Block(0, str(datetime.datetime.now()), "Genesis Block", "0")

    def get_last_block(self):
  
        return self.chain[-1]
