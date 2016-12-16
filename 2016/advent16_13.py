import string

class Maze:
        def __init__(self):
            self.clear()                

        def clear(self):
            self.favorite = 1362
            self.height = 60
            self.width = 60
            self.number_of_open = 0
            self.number_of_walls = 0
            self.number_of_places = 1
            self.places_to_go = ['(1,1)']
            

            

        def test(self):
            self.favorite = 10
            self.height = 10
            self.width = 8
            self.number_of_open = 0
            self.number_of_walls = 0

        def create_room(self):
            self.room = [['.' for x in range(self.width)] for y in range(self.height)]
            self.room_coordinates = [[(x,y) for x in range(self.width)] for y in range(self.height)]
            self.visited_places = ['(1,1)']
            self.visited_walls = []
            self.distance = {'(1,1)':0}
            
        def doStuff(self):
            self.test()
            self.clear()
            self.create_room()

            for x in range(0, self.width):
                for y in range(0, self.height):
                    self.room[y][x] = self.openOrWall(self.room_coordinates[y][x])

#            self.room[39][31] = 'X'
 #           self.room[1][1] = 'X'
   #         for line in self.room:
    #            print line


        def doStuffTwo(self):
                counter = 0                
                while len(self.places_to_go)>0:
                        counter+=1
                        coordinates = self.places_to_go.pop(0)                
                        distance = self.distance[str(coordinates).replace(" ","")]
                        if distance < 51:
                                test = tuple(coordinates[1:-1].split(','))
                                x,y = test
                                x,y = int(x), int(y)
                                places = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
                                self.placesToVisit(places, distance+1)
                                
                                self.walkTo((x,y))

                print 'besokta platser = ', len(self.visited_places)
                print 'varv = ', counter
                print '138 = correct....'


        def placesToVisit(self, places, distance):
                for place in places:
                        test_x, test_y = place
                        if test_x >= 0 and test_y >= 0:
                                place = str(place).replace(" ","")
                                if place not in self.visited_places:
                                        if place not in self.visited_walls:
                                            if self.room[test_y][test_x] == '.':
                                                if place not in self.places_to_go:
                                                        self.places_to_go.append(place)
                                                        self.distance[place] = distance
        
        def walkTo(self, coordinate):
                x,y = coordinate
                coordinate = str(coordinate).replace(" ","")
                if coordinate in self.visited_places:
                        return
                if self.room[y][x] == '#':
                        self.visited_walls.append(coordinate)
                        return
                elif self.room[y][x] == '.':
                        self.visited_places.append(coordinate)
            
        def openOrWall(self, coordinate):
            x,y = coordinate
            value = x*x + 3*x + 2*x*y + y + y*y 
            value = value + self.favorite
            value = bin(value)
            number = value.count('1')
            if number % 2 == 0:
                self.number_of_open+=1
                return '.'
            else:
                self.number_of_walls+=1
                return '#'
                        
if __name__ == "__main__":
        x = Maze()
        x.doStuff()
        x.doStuffTwo()
