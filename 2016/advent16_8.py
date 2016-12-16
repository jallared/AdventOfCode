import string

class TwoFactorAuthentication:
        def __init__(self):
                self.width = 50
                self.height = 6
                self.instructions = []
                self.number_of_lights = 0

        def createScreen(self):
                self.screen = [[0 for x in range(self.width)] for y in range(self.height)]
                self.display = [['.' for x in range(self.width)] for y in range(self.height)] 
                
        def readFile(self):
                input = open('input16_8.txt', 'r')
                for line in input:
                        self.instructions.append(line.strip())
                input.close()
                
        def testInput(self):
                self.width = 7
                self.height = 3
                self.instructions = ['rect 3x2',
                                    'rotate column x=1 by 1',
                                    'rotate row y=0 by 4',
                                    'rotate column x=1 by 1']
                                         
        def doStuff(self):
                self.readFile()
                self.createScreen()
                for instruction in self.instructions:
                        if instruction[0:4] == 'rect':
                                self.light_rectangle(instruction[5:])
                        elif instruction[0:10] == 'rotate row':
                                self.rotate_row(instruction[11:])
                        elif instruction[0:13] == 'rotate column':
                                self.rotate_column(instruction[14:])
                for i in range(0, self.height):
                        for j in range(0, self.width):
                                if self.screen[i][j] == 1:
                                        self.number_of_lights += 1
                                        self.display[i][j] = '#'
                        print self.screen[i]
                print self.number_of_lights
                for row in self.display:
                        print row

                                
        def rotate_row(self, instruction):
                row, distance = instruction.split(' by ')
                temp_row = []
                distance = int(distance)
                if distance < 1:
                        return
                row = int(row.split('=')[1])
                for tut in self.screen[row]:
                        temp_row.append(tut)
                for i in range(0, self.width):
                        self.screen[row][i] = temp_row[i-distance]

        def rotate_column(self, instruction):
                column, distance = instruction.split(' by ')
                distance = int(distance)
                if distance < 1:
                        return 
                column = int(column.split('=')[1])
                temp_column = []
                for row in self.screen:
                        temp_column.append(row[column])
                for i in range(0, self.height):
                        self.screen[i][column] = temp_column[i-distance]
                
                
        def light_rectangle(self, dimensions):
                columns, rows = dimensions.split('x')
                columns, rows = int(columns), int(rows)
                for x in range(columns):
                        for y in range(rows):
                                self.screen[y][x] = 1
               
if __name__ == "__main__":
        x = TwoFactorAuthentication()
        x.doStuff()
