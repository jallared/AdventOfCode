import string

class Decompress:
        def __init__(self):
                self.data = ''
                self.svar = ''
                self.readFile()

        def readFile(self):
                self.data = ''
                self.svar = ''

                input = open('input16_9.txt', 'r')
                for line in input:
                        self.data = line.strip().strip(' ')
                input.close()
                
        def doStuff(self):

                self.readFile()
                strang = self.data
                start_index = strang.find('(')

                        
                while start_index > -1:
                        pre_index, strang = strang[:start_index], strang[start_index:]
                        self.svar += pre_index
                        slut_index = strang.find(')')
                        instruktion, strang = strang[:slut_index+1], strang[slut_index+1:]
                        instruktion = instruktion[1:-1]
                        length, multipel = instruktion.split('x')
                        length = int(length)
                        multipel = int(multipel)
                        multipliceringsstrang, strang = strang[:length], strang[length:]
                                
                        for i in range(0, multipel):
                                self.svar += multipliceringsstrang

                        start_index = strang.find('(')
                self.svar += strang

                print len(self.svar)

        def doStuffOther(self):
                self.readFile()
                weights = []
                for x in self.data:
                        weights.append(1)
                svar = 0
                position = 0
                while position < len(self.data):
                        tecken = self.data[position]
                        if tecken == '(':
                                weight = weights[position]
                                temp = self.data[position:]
                                instruction = temp.split(')',1)[0].strip('(')
                                length, multipel = instruction.split('x')
                                length = int(length)
                                multipel = int(multipel) 
                                position += len(instruction)+2
                                
                                for j in range(0, length):
                                        
                                        old_weight = weights[position+j]
                                        weights[position+j] = old_weight * multipel
                                
                        else:
                                svar += weights[position]
                                position += 1
                print svar
                        
if __name__ == "__main__":
        x = Decompress()
        x.doStuff()
        x.doStuffOther()
