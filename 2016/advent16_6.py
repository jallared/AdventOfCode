import string


class Repeater:
        def __init__(self):
                self.first_message = ''
                self.second_message = ''
                self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                self.strings = ["","","","","","","",""]
                self.test_strings = ["","","","","",""]

        def readFile(self):
                input = open('input16_6.txt', 'r')
                for line in input:
                        i = 0
                        for letter in line.strip():
                                self.strings[i] += letter
                                i += 1
                input.close()
                
        def readFileTest(self):
                input = open('input16_6_test.txt', 'r')
                for line in input:
                        i = 0
                        for letter in line.strip():
                                self.test_strings[i] += letter
                                i += 1
                input.close()
                
        def doStuffTest(self):
                self.readFileTest()
                self.first_message = ""
                self.second_message = ""
                for test_string in self.test_strings:
                        self.first_message += self.find_commonest_letter(test_string)
                        self.second_message += self.find_least_commonest_letter(test_string)
                print self.first_message
                print self.second_message

        def doStuff(self):
                self.readFile()
                self.first_message = ""
                self.second_message = ""
                for string in self.strings:
                        self.first_message += self.find_commonest_letter(string)
                        self.second_message += self.find_least_commonest_letter(string)
                print self.first_message
                print self.second_message
        
        
        def find_commonest_letter(self, input_string):
                all_letters = []
                for letter in self.alphabet:
                        count = input_string.count(letter)
                        all_letters.append((letter, count))
                sorted_list = sorted(all_letters, key=lambda x: x[1], reverse=True)
                return sorted_list[0][0]

        def find_least_commonest_letter(self, input_string):
                all_letters = []
                for letter in self.alphabet:
                        count = input_string.count(letter)
                        if count > 0:
                                all_letters.append((letter, count))
                sorted_list = sorted(all_letters, key=lambda x: x[1])
                return sorted_list[0][0]


if __name__ == "__main__":
        x = Repeater()
        x.doStuffTest()
        x.doStuff()
