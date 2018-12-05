import string
import copy
		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.distributions = []
			self.start_distribution = []
			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			for row in input:
				self.start_distribution = list(map(int, row.split("\t")))
				
			input.close()

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			#self.read_instructions('input17_5_t.txt')
			self.start_distribution = [0,2,7,0]
			self.memoryAllocation()
		
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_instructions('input17_6.txt')
			self.memoryAllocation()
			
		def memoryAllocation(self):
			tryes = 0
			self.distributions.append(self.start_distribution)
			current_distribution = copy.deepcopy(self.start_distribution)
			final_distribution_found = False
			new_distribution = []
			while not final_distribution_found:
				tryes+=1
				new_distribution = self.calculateNewDistribution(current_distribution)
				try:
					self.distributions.index(new_distribution)
					final_distribution_found = True
				except:
					temp = copy.deepcopy(new_distribution)
					self.distributions.append(temp)
				
			print (tryes)
			print (len(self.distributions) - self.distributions.index(new_distribution))
			
				
		def calculateNewDistribution(self, distribution):
			index = distribution.index(max(distribution))
			cell_value = distribution[index]
			distribution[index] = 0
			index+=1
			new_distribution = self.redistributeCell(distribution, cell_value, index)
			return (new_distribution)
			
		def redistributeCell(self, distribution, value, index):
			while value > 0:
				if index >= len(distribution):
					index = 0
				distribution[index]+=1
				value-=1
				index+=1
			return distribution
				
				
				
		
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
#		x.testStuffTwo()
		x.doStuff()
