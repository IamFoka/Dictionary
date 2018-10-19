from linked_list import LinkedList
from node import Node

class FirstLayer:
    def __init__(self):
        self.vector = []
        
    @staticmethod
    def make_first_layer():
        layer = FirstLayer()
        layer.populate()
        return layer

    def populate(self):
        for i in range(26):
            self.vector.append(LinkedList())
    
    def add(self, word):
        node = Node(word)
        position = ord(word[0]) - ord('a')
        self.vector[position].add(node)

    def remove(self, word):
        node = Node(word)
        position = ord(word[0]) - ord('a')
        self.vector[position].remove(node)

    def total_amount_words(self):
        total = 0

        for i in self.vector:
            total += i.amount
        
        return total

    def read_all(self):
        for i in self.vector:
            i.read()

    def read_by_letter(self, letter):
        if len(letter) > 1:
            print("You must enter just one letter")
            return

        position = ord(letter) - ord('a')

        self.vector[position].read()

    def all_words_amount(self):
        amount = 0

        for i in self.vector:
            amount += i.amount

        return amount   

    def all_words_amount_by_letter(self, letter):
        if len(letter) > 1:
            print("You must enter just one letter")
            return
        
        position = ord(letter) - ord('a')

        return self.vector[position].amount

    



        
