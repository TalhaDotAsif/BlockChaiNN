import hashlib
from blockchain import Block
blockchain = []

genesis_block = Block("Chancellor on the brink ....",["Satoshi sent 1 BTC to Ivan", "Satoshi send 5 BTC to Hal Finney"])
second_block = Block(genesis_block.block_hash,["Ivan sent 5 BTC to Liz","John sent 5 BTC to Jenny"])
third_block = Block(second_block.block_hash,["La la Land"])
print("Block Hash: Genesis Block")
print(genesis_block.block_hash)
print("Block Hash: Second Block")
print(second_block.block_hash)
print("Block Hash: Third Block")
print(third_block.block_hash)