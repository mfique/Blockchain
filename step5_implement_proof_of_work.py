from step4_develop_the_blockchain_class import BlockchainWithValidation

class BlockchainWithPoW(BlockchainWithValidation):
    def proof_of_work(self, block):
        
        block.proof = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * self.difficulty): 
            block.proof += 1
            computed_hash = block.compute_hash()
        return computed_hash