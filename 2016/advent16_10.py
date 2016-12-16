import string

class Zoom:
        def __init__(self):
                self.clear()
                

        def clear(self):
                self.init_values = []
                self.instructions = []

        def readFile(self):
                self.clear()
                input = open('input16_10.txt', 'r')
                for line in input:
                        instruktion = line.strip()
                        if instruktion.find('value') > -1:
                                self.init_values.append(instruktion)
                        else:
                                self.instructions.append(instruktion)
                input.close()

        def testInput(self):
                self.clear()
                data = ['value 5 goes to bot 2',
                        'bot 2 gives low to bot 1 and high to bot 0',
                        'value 3 goes to bot 1',
                        'bot 1 gives low to output 1 and high to bot 0',
                        'bot 0 gives low to output 2 and high to output 0',
                        'value 2 goes to bot 2']

                for line in data:
                        instruktion = line.strip()
                        if instruktion.find('value') > -1:
                                self.init_values.append(instruktion)
                        else:
                                self.instructions.append(instruktion)
                
        def doStuff(self):

                self.testInput()
                print 'initiera allt'
                print 'processa alla instruktioner'
                print 'luska ut vilken bot som har chip 61 och 17 samtidigt?'
                

        def initiateBotsAndGiveChips(self):
                print 'skapa alla botar och ge dem sina startchips'
                print 'Kan ha lista med tupler, [(botnamn, (chip0, chip1))]'

        def processLine(self):
                print 'traska igenom instruktioner och flytta runt chips'

        
                        
if __name__ == "__main__":
        x = Zoom()
        x.doStuff()

129
67
94

68
92
96
124
