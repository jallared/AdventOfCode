import string

		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.instruction_list = []
			self.visited_frequencies = []
			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			for instruction in input:
				variable = str(instruction.strip('\n'))
				self.instruction_list.append(int(variable))
			input.close()			

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input_1_t.txt')
			print(self.sumDigitsOne(0))
		
		def testStuffTwo(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input_1_t.txt')
			print(self.sumDigitsTwo())
			
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_instructions('input_1.txt')
			print(self.sumDigitsOne(0))
			print(self.sumDigitsTwo())
			
		def sumDigitsOne(self, starting_frequency):
			frequency = starting_frequency
			for frequency_diff in self.instruction_list:
				frequency += frequency_diff
			return frequency
				
		def sumDigitsTwo(self):
			frequency = 0
			self.visited_frequencies.append(frequency)
			while True:
				for frequency_diff in self.instruction_list:
					frequency += frequency_diff
					if frequency in self.visited_frequencies:
						return frequency
					else:
						self.visited_frequencies.append(frequency)
			
	
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
		x.testStuffTwo()
		x.doStuff()
