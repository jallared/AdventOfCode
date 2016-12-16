import string
	
class Lighting:
	def __init__(self):
		self.lights = [[0 for x in range(1000)] for x in range(1000)]
		
		#self.sexEtt()
		self.sexTva()
		
		
	def sexEtt(self):
		input = open('input_6.txt', 'r')
		instruction=0
		for row in input:
			print instruction
			instruction+=1
			new_row = row.split(" ")
			if new_row[0] == 'turn':
				if new_row[1] == 'on':
					x_start,y_start = map(int, new_row[2].split(","))
					x_end,y_end = map(int, new_row[4].split(","))
					self.turn_on(x_start,y_start,x_end,y_end)
					
				if new_row[1] == 'off':
					x_start,y_start = map(int, new_row[2].split(","))
					x_end,y_end = map(int, new_row[4].split(","))
					self.turn_off(x_start,y_start,x_end,y_end)
					
			else:
				x_start,y_start = map(int, new_row[1].split(","))
				x_end,y_end = map(int, new_row[3].split(","))
				self.toggle(x_start,y_start,x_end,y_end)
					
			
		num=0
		for x in range(0,1000,1):
			for y in range(0,1000,1):
				if self.lights[x][y]:
					num+=1
		print num
	
	def sexTva(self):
		input = open('input_6.txt', 'r')
		instruction=0
		for row in input:
			print instruction
			instruction+=1
			new_row = row.split(" ")
			if new_row[0] == 'turn':
				if new_row[1] == 'on':
					x_start,y_start = map(int, new_row[2].split(","))
					x_end,y_end = map(int, new_row[4].split(","))
					self.turn_on2(x_start,y_start,x_end,y_end)
					
				if new_row[1] == 'off':
					x_start,y_start = map(int, new_row[2].split(","))
					x_end,y_end = map(int, new_row[4].split(","))
					self.turn_off2(x_start,y_start,x_end,y_end)
					
			else:
				x_start,y_start = map(int, new_row[1].split(","))
				x_end,y_end = map(int, new_row[3].split(","))
				self.toggle2(x_start,y_start,x_end,y_end)
					
			
		num=0
		for x in range(0,1000,1):
			for y in range(0,1000,1):
				num+=self.lights[x][y]
					
		print num	
				
	def turn_on(self, x_start, y_start, x_end, y_end):
	
		for x in range(x_start,x_end+1,1):
			for y in range(y_start,y_end+1,1):
				self.lights[x][y] = 1
		

	def turn_off(self, x_start, y_start, x_end, y_end):
	
		for x in range(x_start,x_end+1,1):
			for y in range(y_start,y_end+1,1):
				self.lights[x][y] = 0
						
	def toggle(self, x_start, y_start, x_end, y_end):
		
		for x in range(x_start,x_end+1,1):
			for y in range(y_start,y_end+1,1):
				if self.lights[x][y] == 1:
					self.lights[x][y] = 0
				elif self.lights[x][y] == 0:
					self.lights[x][y] = 1
				
	def turn_on2(self, x_start, y_start, x_end, y_end):
	
		for x in range(x_start,x_end+1,1):
			for y in range(y_start,y_end+1,1):
				self.lights[x][y] += 1
		

	def turn_off2(self, x_start, y_start, x_end, y_end):
	
		for x in range(x_start,x_end+1,1):
			for y in range(y_start,y_end+1,1):
				if self.lights[x][y] > 0:
					self.lights[x][y] -= 1
			
						
	def toggle2(self, x_start, y_start, x_end, y_end):
		
		for x in range(x_start,x_end+1,1):
			for y in range(y_start,y_end+1,1):
				self.lights[x][y] += 2
				
	

		
if __name__ == "__main__":
	x = Lighting()