import string

robot_x = 0
robot_y = 0
tomte_x = 0
tomte_y = 0
plats = (tomte_x, tomte_y)

paketerad_plats = []
def lagg_paket(plats):	
	paketerad_plats.append(plats)
	
lagg_paket(plats)
lagg_paket(plats)

	
input = open('input_3.txt', 'r')
number = 0
for row in input:
	while number < len(row) -1:
		sign = row[number]
		number+=1
		if sign == '^':
			tomte_y = tomte_y + 1
		elif sign == 'v':
			tomte_y = tomte_y -1
		elif sign == '>':
			tomte_x = tomte_x + 1
		elif sign == '<':
			tomte_x = tomte_x -1
		plats = (tomte_x,tomte_y)
		lagg_paket(plats)
		sign = row[number]
		number+=1
		if sign == '^':
			robot_y = robot_y + 1
		elif sign == 'v':
			robot_y = robot_y -1
		elif sign == '>':
			robot_x = robot_x + 1
		elif sign == '<':
			robot_x = robot_x -1
		plats = (robot_x,robot_y)
		lagg_paket(plats)
input.close()

alla_hus = list(set(paketerad_plats))
print len(alla_hus)
print number
