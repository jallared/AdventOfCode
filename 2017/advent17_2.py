import string

		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.instruction_list = []
			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			for instruction in input:
				row = instruction.strip("\n").split("\t")
				row = list(map(int, row))
				self.instruction_list.append(row)
				
			input.close()

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input17_2_t.txt')
			self.calculateChecksumOne()
		
		def testStuffTwo(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input17_2_2_t.txt')
			self.calculateChecksumTwo()
			
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_instructions('input17_2.txt')
			self.calculateChecksumOne()
			self.calculateChecksumTwo()
			
		def calculateChecksumOne(self):
			checksum = 0
			for row in self.instruction_list:
				row.sort()
				checksum+= (row[-1] - row[0])
			print (checksum)
		
			
		def calculateChecksumTwo(self):
			checksum = 0
			for row in self.instruction_list:
				for index in range(len(row)):
					divisor = row[index]
					for index2 in range(len(row)):
						if index2 != index:
							dividend = row[index2]
							if dividend % divisor == 0:
								checksum+=int(dividend/divisor)
			print (checksum)
			
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
		x.testStuffTwo()
		x.doStuff()
