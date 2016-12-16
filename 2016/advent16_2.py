import string


class KeyPad:
        def __init__(self):
                self.x, self.y = 0, 0
                self.numbers = []
                self.instructions = []
                self.legalNumbersOne = [(0,0), (1,0), (2,0), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2)]
                self.keyPadOne = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                self.legalNumbersTwo = [(2,0), (1,1), (2,1), (3,1), (0,2), (1,2), (2,2), (3,2), (4,2), (1,3), (2,3), (3,3), (2,4)]
                self.keyPadTwo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D']
                
        def readFile(self):
                input = open('input16_2.txt', 'r')
                self.instructions = []
                for line in input:
                        self.instructions.append(line.strip())
                input.close()

        def doStuff(self, x, y, text, version, instructions = None):
                self.x, self.y = x, y
                self.numbers = []
                
                if version == 'ett':
                        self.legalNumbers = self.legalNumbersOne
                        self.keyPad = self.keyPadOne
                        self.readFile()
                elif version == 'tva':
                        self.legalNumbers = self.legalNumbersTwo
                        self.keyPad = self.keyPadTwo
                        self.readFile()
                elif version == 'test ett':
                        self.legalNumbers = self.legalNumbersOne
                        self.keyPad = self.keyPadOne
                        self.instructions = instructions
                elif version == 'test tva':
                        self.legalNumbers = self.legalNumbersTwo
                        self.keyPad = self.keyPadTwo
                        self.instructions = instructions
                else:
                        return
                for instruction in self.instructions:
                        for sign in instruction:
                                self.move(sign)
                        self.numbers.append((self.x, self.y))
                answer = []
                for number in self.numbers:
                        answer.append(self.keyPad[self.legalNumbers.index(number)])
                print text, answer


        def move(self, sign):
                if sign == 'U':
                        if self.legalNumbers.count((self.x, self.y-1)) > 0:
                                self.y -= 1
                elif sign == 'D':
                        if self.legalNumbers.count((self.x, self.y+1)) > 0:
                                self.y += 1        
                elif sign == 'L':
                        if self.legalNumbers.count((self.x-1, self.y)) > 0:
                                self.x -= 1
                elif sign == 'R':
                        if self.legalNumbers.count((self.x+1, self.y)) > 0:
                                self.x += 1

if __name__ == "__main__":
        x = KeyPad()
        x.doStuff(1,1, 'Instruktion test ett: ', 'test ett', instructions = ['ULL', 'RRDDD', 'LURDL', 'UUUUD'])
        x.doStuff(0,2, 'Instruktion test tva: ', 'test tva', instructions = ['ULL', 'RRDDD', 'LURDL', 'UUUUD'])
        x.doStuff(1,1, 'Instruktion ett: ', 'ett')
        x.doStuff(0,2, 'Instruktion tva: ', 'tva')
                
        
