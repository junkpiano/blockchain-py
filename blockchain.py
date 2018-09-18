#!/usr/bin/env python

import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        genesis = Block(0, date.datetime.now(), "Genesis Block", "0")
        self.blocks = [genesis]
        self.lastBlock = genesis

    def next_block(self):
        block = Block(self.lastBlock.index + 1,
                     date.datetime.now(),
                     "Next Block",
                     self.lastBlock.hash)
        self.blocks.append(block)
        self.lastBlock = block
        return block
    
if __name__ == "__main__":
    num_of_blocks_to_add = 20
    bc = BlockChain()
    
    for i in range(0, num_of_blocks_to_add):
        next_block = bc.next_block()
        print("index #{}. New Node {}\nprevious node: {}".format(next_block.index,
                                                                 next_block.hash,
                                                                 next_block.previous_hash))
