from first_list import FirstLayer
from linked_list import LinkedList

class Interface:
    def __init__(self):
        self.main_list = FirstLayer.make_first_layer()
        self.most_recurring = list()

    def menu(self):
        while(True):
            print("\n-------Menu-------")
            print("0. Exit")
            print("1. Insert Words")
            print("2. Remove word")
            print("3. Read all words")
            print("4. Read all words by letter")
            print("5. Show all words amount")
            print("6. Show all words amount by letter")
            print("7. Show show more recurring words")
            print("8. Clear words")
            
            try:
                menu = int(input())
            except ValueError:
                print("You must enter one of the options")

            if(menu < 0 or menu > 8):
                print("You must enter one of the options")

            if(menu == 0):
                break

            if(menu == 1):
                word = None
                print("Enter '0' to stop")
                while(word != '0'):
                    word = input("\nEnter your word:")

                    if(word == '0'):
                        break
                        
                    word = word.lower()
                    word.strip()
                    self.main_list.add(word)

            if(menu == 2):
                word = input("\nEnter your word:")
                word = word.lower()
                word.strip()

                self.main_list.remove(word)

            if(menu == 3):
                self.main_list.read_all()

            if(menu == 4):
                letter = input("\nEnter your letter:")
                letter = letter.lower()
                letter.strip()

                self.main_list.read_by_letter(letter)

            if(menu == 5):
                print("\nAll words amount: ", self.main_list.all_words_amount())

            if(menu == 6):
                letter = input("\nEnter your letter:")
                letter = letter.lower()
                letter.strip()

                print("\n All words starting with ", letter, " amount: ", self.main_list.all_words_amount_by_letter(letter))

            if(menu == 7):
                higher_amount = 1
                self.most_recurring = list()
   
                for i in range(26):
                    self.main_list.vector[i].recurrence_words()

                for i in range(26):
                    if(self.main_list.vector[i].start != None):
                        if(self.main_list.vector[i].most_recurrences[0].amount > higher_amount):
                            self.most_recurring = list()
                            for j in self.main_list.vector[i].most_recurrences:
                                self.most_recurring.append(j)
                            
                            higher_amount = self.main_list.vector[i].most_recurrences[0].amount
                        elif(self.main_list.vector[i].most_recurrences[0].amount == higher_amount):
                            for y in self.main_list.vector[i].most_recurrences:
                                self.most_recurring.append(y)

                for i in self.most_recurring:
                    print("word: ", i.data, " occurrences: ", i.amount)

            if(menu == 8):
                self.main_list = FirstLayer.make_first_layer()
                self.most_recurring = list()
                    
            print("\n\n\n")


                