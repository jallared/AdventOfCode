import string

		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.instruction_list = []
			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			for instruction in input:
				variable = str(instruction.strip('\n'))
				self.instruction_list.append(variable)
			input.close()

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input17_1_t.txt')
			self.sumDigitsOne()
		
		def testStuffTwo(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input17_1_2_t.txt')
			self.sumDigitsTwo()
			
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_instructions('input17_1.txt')
			self.sumDigitsOne()
			self.sumDigitsTwo()
			
		def sumDigitsOne(self):
			for row in self.instruction_list:
				summa = 0
				length = len(row)
				for index in range(length):
					if (index+1) == length:
						if row[index] == row[0]:
							summa+=int(row[index])
					elif (index+1) < length:
						if row[index] == row[index+1]:
							summa+=int(row[index])
				print (summa)
				
		def sumDigitsTwo(self):
			for row in self.instruction_list:
				summa = 0
				length = len(row)
#				print ('length = ', length)
				compare = int(length/2)
				for index in range(compare):
					if row[index] == row[index+compare]:
						summa = summa + 2*(int(row[index]))
				print (summa)
			
	
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
		x.testStuffTwo()
		x.doStuff()
