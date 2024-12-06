from step3_create_the_genesis_block import Blockchain

class BlockchainWithValidation(Blockchain):
    def add_block(self, new_block):
      
        new_block.previous_hash = self.get_last_block().hash
        new_block.hash = new_block.compute_hash()  # Recalculate hash with updated previous_hash
        self.chain.append(new_block)

    def is_chain_valid(self):
     
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

          
            if current_block.hash != current_block.compute_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
