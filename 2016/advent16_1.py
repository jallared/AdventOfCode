import string


input = open('input16_1.txt', 'r')
position_x = 0
position_y = 0
visited_places = [(0,0)]
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
direction_number = 0
secret_location_found = False
for instruction in input:
        instruction_list = instruction.split(',')

for instruction in instruction_list:
        instruction = instruction.strip(' ')
        first = instruction[0]
        length = int(instruction[1:])
        
        if first == 'L':
                direction_number -= 1
                if direction_number == -1:
                        direction_number = 3
                #print directions[direction_number], length
        elif first == 'R':
                direction_number += 1
                if direction_number == 4:
                        direction_number = 0
                #print directions[direction_number], length

        for i in range(0, length):
                
                if directions[direction_number] == 'NORTH':
                        position_y += 1
                elif directions[direction_number] == 'EAST':
                        position_x += 1
                elif directions[direction_number] == 'SOUTH':
                        position_y -= 1
                elif directions[direction_number] == 'WEST':
                        position_x -= 1
                if secret_location_found == False:
                        if visited_places.count((position_x, position_y)) > 0:
                                secret_location = position_x, position_y
                                secret_location_found = True
                        else:
                                visited_places.append((position_x, position_y))
print "End of the line: ", (position_x, position_y)
print "End of the line distance: ", abs(position_x)+abs(position_y)
print "Secret location: ", secret_location
print "Secret location distace: ", abs(secret_location[0])+abs(secret_location[1])
input.close()
