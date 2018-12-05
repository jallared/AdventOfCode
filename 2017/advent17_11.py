import string
import copy
import sys 
		
class Stuff:
		def __init__(self):
			self.clear()

		def clear(self):
			self.instructions = []
			
		def read_instructions_one(self, file_name):
			input = open(file_name, 'r')
			for row in input:
				self.instructions = row.strip("\n").split(",")
			input.close()
						
		def doStuff(self):
			self.clear()
			self.read_instructions_one('input17_11.txt')
			x,y,z,distance = 0,0,0,0
			distances = []
			
			for temp in self.instructions:
				if temp == 'nw':
					x-=1
					y+=1
				elif temp == 'n':
					y+=1
					z-=1
				elif temp == 'ne':
					x+=1
					z-=1
				elif temp == 'se':
					x+=1
					y-=1
				elif temp == 's':
					y-=1
					z+=1
				elif temp == 'sw':
					x-=1
					z+=1
				
				if (x+y+z != 0):
					print ('TUT')
					
				
				distance = int((abs(x)+abs(y)+abs(z))/2)
				distances.append(distance)
				
			print ('stopp = ', distances[-1])
			print ('riktigt avstånd = 715')	
			print ('1206 är för lågt')
			print ('1159 är för lågt')
			print ('svar = ', max(distances))		
		
if __name__ == "__main__":
		x = Stuff()
		x.doStuff()
