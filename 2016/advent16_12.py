import string

class Assembunny:
        def __init__(self):
                self.clear()                

        def clear(self):
                self.init_values = []
                self.instructions = []
                #self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0} #part 1
                self.registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0} #part 2

        def readFile(self):
                self.clear()
                input = open('input16_12.txt', 'r')
                for line in input:
                        instruktion = line.strip()
                        self.instructions.append(instruktion)
                input.close()

        def testInput(self):
                self.clear()
                data = ['cpy 41 a',
                        'inc a',
                        'inc a',
                        'dec a',
                        'jnz a 2',
                        'dec a',
                        'break']

                for line in data:
                        instruktion = line.strip()
                        self.instructions.append(instruktion)
                
        def doStuff(self):
#                self.testInput()
                self.readFile()
                index = 0
                print len(self.instructions)
                while self.instructions[index] != 'break':
                        instruktion = self.instructions[index]
                        if instruktion[:3] == 'cpy':
                                self.copy(instruktion)
                                index += 1
                        elif instruktion[:3] == 'inc':
                                self.increment(instruktion)
                                index += 1
                        elif instruktion[:3] == 'dec':
                                self.decrement(instruktion)
                                index += 1
                        elif instruktion[:3] == 'jnz':
                                index += self.jump(instruktion)
                        else:
                                print 'OH NO!'
                                break

                print self.registers

                
        def copy(self, instruktion):
                dummy, summa, variabel = instruktion.split(' ')
                try:
                        summa = int(summa)
                except:
                        summa = self.registers[summa]

                self.registers[variabel] = summa

        def increment(self, instruktion):
                dummy, variabel = instruktion.split(' ')
                self.registers[variabel] += 1
        
        def decrement(self, instruktion):
                dummy, variabel = instruktion.split(' ')
                self.registers[variabel] -= 1

        def jump(self, instruktion):
                dummy, variabel, distans = instruktion.split(' ')
                try:
                        variabel = self.registers[variabel]
                except:
                        variabel = int(variabel)
                if variabel == 0:
                        return 1
                else:
                        return int(distans)

                        
if __name__ == "__main__":
        x = Assembunny()
        x.doStuff()
