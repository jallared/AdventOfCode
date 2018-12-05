import string
import copy
import sys 
		
class Stuff:
		def __init__(self):
			self.clear()
			
		def clear(self):
			self.factor_a = 16807
			self.factor_b = 48271
			self.a_values = []
			self.b_values = []
			
			
		def testStuffOne(self):
			self.clear()
			start_value_a = 65
			start_value_b = 8921
			self.calculatePairs(start_value_a, start_value_b, 5) #40000000
		
		def testStuffTwo(self):
			self.clear()
			start_value_a = 65
			start_value_b = 8921
			a_list = self.calculateLists(start_value_a, self.factor_a, 5000000, 4)
			b_list = self.calculateLists(start_value_b, self.factor_b, 5000000, 8)
			temp = 0
			for i in range(5000000):
				if a_list[i] == b_list[i]:
					temp+=1
			print (temp)

		def doStuffTwo(self):
			self.clear()
			start_value_a = 116
			start_value_b = 299
			a_list = self.calculateLists(start_value_a, self.factor_a, 5000000, 4)
			b_list = self.calculateLists(start_value_b, self.factor_b, 5000000, 8)
			temp = 0
			for i in range(5000000):
				if a_list[i] == b_list[i]:
					temp+=1
			print (temp)

			
		def doStuff(self):
			self.clear()
			start_value_a = 116
			start_value_b = 299
			self.calculatePairs(start_value_a, start_value_b, 40000000)
				
		def calculatePairs(self, start_value_a, start_value_b, iterations):
			temp = 0
			next_value_a = start_value_a
			next_value_b = start_value_b
			for i in range(iterations):
				next_value_a = self.generateValue(next_value_a, self.factor_a)
				next_value_b = self.generateValue(next_value_b, self.factor_b)
				binary_a = bin(next_value_a).split('b')[1][-16:]
				binary_b = bin(next_value_b).split('b')[1][-16:]
				if binary_a == binary_b:
					temp+=1
			print (temp)
				
		def calculateLists(self, start_value, factor, iterations, criteria):
			next_value = start_value
			return_list = []
			while (len(return_list) < iterations):
				next_value = self.generateValue(next_value, factor)
				if next_value % criteria == 0:
					return_list.append(bin(next_value).split('b')[1][-16:])
			return return_list
				
		def generateValue(self, previous_value, factor):
			value = previous_value*factor
			next_value = value % 2147483647
			return next_value
			
if __name__ == "__main__":
		x = Stuff()
		#x.testStuffOne()
		#x.doStuff()
		#x.testStuffTwo()
		#x.doStuffTwo()