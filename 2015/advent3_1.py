import string

x = 0
y = 0
plats = (x,y)

paketerad_plats = []
def lagg_paket(plats):	
	paketerad_plats.append(plats)
	
lagg_paket(plats)

	
input = open('input_3.txt', 'r')
number = 0
for row in input:
	for number in range(0,len(row),1):
		sign = row[number]
		number+=1
		if sign == '^':
			y = y + 1
		elif sign == 'v':
			y = y -1
		elif sign == '>':
			x = x + 1
		elif sign == '<':
			x = x -1
		plats = (x,y)
		lagg_paket(plats)
		
input.close()

alla_hus = list(set(paketerad_plats))
print len(alla_hus)

