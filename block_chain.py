import datetime
import json
import hashlib
from time import time
from uuid import uuid4


class BlockChain(object):

    def __init__(self):
        self.chain = []
        self.current_transaction = []

        # initiate the block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=100):
        # create a new Block and add it to chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'transactions': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chin[-1])
        }
        # reset current transaction
        self.current_transaction = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, receiver, amount):
        # add a new transaction to transaction list
        """
        :param sender: identity of the previous sender
        :param receiver: identity of next receiver
        :param amount: amount
        :return: the index of the Block that holding the this transaction
        """
        self.current_transaction.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # hash a Block
        block_sting = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_sting).hexdigest()

    @property
    def last_block(self):
        # return the last block in the chain
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        generate a SHA-256 value for the block
        :param block: <dict> Block
        :return: <str>
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        simple proof of working algorithm
        - find a number p which its hash(pp') contains 4 leading zero, where p is the
        previous p'
        - p is the previous proof and p' is the new  proof
        :param last_proof:
        :return:
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

    @staticmethod
    def valid_proof(last_proof, proof):
        """

        :param last_proof:  int
        :param proof:  int
        :return: bool
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'