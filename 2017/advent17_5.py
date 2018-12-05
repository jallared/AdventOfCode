import string

		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.instructions = []
			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			for row in input:
				number = int(row.strip("\n"))
				#row = list(map(int, row))
				self.instructions.append(number)
				
			input.close()

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input17_5_t.txt')
			self.findExit()
		
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_instructions('input17_5.txt')
			self.findExit()
			
		def findExit(self):
			tryes = 0
			length = len(self.instructions)
			position = 0
			while position < length:
				instruction = self.instructions[position]
				if instruction > 2:
					self.instructions[position]-=1
				else:
					self.instructions[position]+=1
				tryes+=1
				position+=instruction
				
			print (tryes)

if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
#		x.testStuffTwo()
		x.doStuff()
