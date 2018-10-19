class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.amount = 0
        self.most_recurrences = []

    def add(self, node):
        it = self.start

        if self.start == None:
            self.start = node
            self.end = node
            self.amount += 1
            node.amount += 1
            return

        if it.data == node.data:
            self.amount += 1
            it.amount += 1
            return

        if self.compare(node.data, it.data):
            node.next = self.start
            self.end = self.start
            self.start = node
            self.amount += 1
            node.amount += 1
            return

        while True:
            if it.data == node.data:
                self.amount += 1
                it.amount += 1
                return
            elif it.next != None and it.next.data == node.data:
                self.amount += 1
                it.next.amount += 1
                return
            elif it.next != None and self.compare(node.data, it.next.data):
                node.next = it.next
                it.next = node
                self.amount += 1
                it.next.amount += 1
                return
            elif it.next == None:
                it.next = node
                self.end = node
                self.amount += 1
                it.next.amount += 1
                return

            
            it = it.next

    def remove(self, node):
        it = self.start

        if self.start == None:
            print("Empty list")
            return

        if it.next == None:
            if it.data == node.data:
                self.amount -= it.amount
                self.start = None
                return
            print("Word not found")
            return
        
        if it.data == node.data:
            self.amount -= it.amount
            self.start = it.next
            return

        while True:
            if it.next != None and it.next.data == node.data:
                if it.next.next != None:
                    self.amount -= it.next.amount
                    it.next = it.next.next
                    return
                it.next = None
                return

            if it.next == None:
                print("Word not found")
                return

            it = it.next

    # def queue(self, node):
    #     if(self.end != None):
    #         self.start = node
    #         self.end = node
    #         return

    #     self.end.next = node
    #     self.end = node
    #     return

    # def dequeue(self, node):
    #     if(self.start == None):
    #         return
        
    #     if(self.end == self.start):
    #         self.end = None
    #         self.start = None
    #         return
    #     self.start = self.start.next

    def read(self):
        it = self.start

        if it == None:
            return
        
        while it != None:
            print('\n\nword: ', it.data, ' occurrences:', it.amount)
            it = it.next
        return    

    def compare(self, node_word, it_word):
        return node_word < it_word

    def recurrence_words(self):
        self.most_recurrences = []
        
        if(self.start != None):
            it = self.start
            higher_amount = 1

            while(it != None):
                if(it.amount > higher_amount):
                    higher_amount = it.amount
                
                it = it.next

            it = self.start

            while(it != None):
                if(it.amount == higher_amount):
                    self.most_recurrences.append(it)

                it = it.next
        
        return

            