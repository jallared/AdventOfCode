import string
import copy
import sys 
		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.dancers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
			self.start_positions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			for row in input:
				self.instructions = row.strip("\n").split(",")

		def doStuff(self):
			self.clear()
			self.read_instructions('input17_16.txt')
			self.dance()
			i = 1
			#for i in range(1000000000):
			while self.dancers != self.start_positions:
				
				self.dance()
				i+=1
			
			rest = 1000000000 % i
			
			for t in range(rest):
				self.dance()
			
			dancers = ''
			for t in self.dancers:
				dancers+=t
			print (dancers)
			
		def testStuffOne(self):
			self.clear()
			self.read_instructions('input17_16_t.txt')
			self.dancers = ['a', 'b', 'c', 'd', 'e']

			self.dance()
			self.dance()
			dancers = ''
			for t in self.dancers:
				dancers+=t
			print (dancers)
		
		def dance(self):
			for instruction in self.instructions:
				move = instruction[0]
				instruction = instruction[1:]
				if move == 's':
					self.spin(instruction)
				elif move == 'x':
					self.swapPosition(instruction)
				elif move == 'p':
					self.swapName(instruction)
				else:
					raise ValueError
		
		def spin(self, instruction):
			places = int(instruction)
			for i in range(places):
				self.dancers.insert(0, self.dancers.pop())
#			print ('Spin! ', instruction)
		
		def swapName(self, instruction):
			swap_1, swap_2 = instruction.split('/')
			a, b = self.dancers.index(swap_1), self.dancers.index(swap_2)
			self.dancers[a], self.dancers[b] = self.dancers[b], self.dancers[a]
			#print (swap_1, ' Ska byta plats med ', swap_2)
			
		def swapPosition(self, instruction):
			swap_1, swap_2 = list(map(int, instruction.split('/')))
			self.dancers[swap_1], self.dancers[swap_2] = self.dancers[swap_2], self.dancers[swap_1]
			
#			print ('Dansare på plats ', swap_1, ' ska byta plats med dansare på plats ', swap_2)
		
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
		x.doStuff()
