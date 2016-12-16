import string


class Triangles:
        def __init__(self):
                self.triangle_list = []
                self.validTriangles = 0
                
        def readFileOne(self):
                input = open('input16_3.txt', 'r')
                for line in input:
                        self.triangle_list.append(line.strip())
                input.close()

        def readFileTwo(self):
                lista_ett = []
                lista_tva = []
                lista_tre = []
                lista = []
                input = open('input16_3.txt', 'r')
                for line in input:
                        line = line.strip()
                        line = line.split()
                        lista_ett.append(int(line[0]))
                        lista_tva.append(int(line[1]))
                        lista_tre.append(int(line[2]))
                input.close()
                for item in lista_ett:
                        lista.append(item)
                for item in lista_tva:
                        lista.append(item)
                for item in lista_tre:
                        lista.append(item)

                self.triangle_list = lista


        def doStuffOne(self):
                self.readFileOne()
                for item in self.triangle_list:
                        #print item
                        [x,y,z] = item.split()
                        x,y,z = int(x), int(y), int(z)
                        #print x,y,z
                        if self.isValid(x,y,z):
                                self.validTriangles +=1

        def doStuffTwo(self):
                self.readFileTwo()
                self.validTriangles = 0
                for i in range(0, len(self.triangle_list), 3):
                        x,y,z = self.triangle_list[i], self.triangle_list[i+1], self.triangle_list[i+2] 
                        if self.isValid(x,y,z):
                                self.validTriangles +=1
                                
        def isValid(self, x, y, z):
                if (x + y > z) and (x + z > y) and (y+z >x):
                        return True
                else:
                        return False

if __name__ == "__main__":
        x = Triangles()
        x.doStuffOne()
        print x.validTriangles
        x.doStuffTwo()
        print x.validTriangles        
