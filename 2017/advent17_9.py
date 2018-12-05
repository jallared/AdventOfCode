import string
import copy
import sys 
		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.skrap = []
			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			stream = []
			for row in input:
				for character in row.strip("\n"):
					stream.append(character)
			input.close()
			return stream

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			test_inputs = [ '{}',
							'{{{}}}',
							'{{},{}}',
							'{{{},{},{{}}}}',
							'{<a>,<a>,<a>,<a>}',
							'{{<ab>},{<ab>},{<ab>},{<ab>}}',
							'{{<!!>},{<!!>},{<!!>},{<!!>}}',
							'{{<a!>},{<a!>},{<a!>},{<ab>}}']
			test_streams = []
			for input in test_inputs:
				temp = []
				for character in input:
					temp.append(character)
				test_streams.append(temp)
				
			test_scores = [1, 6, 5, 16, 1, 9, 9, 3]
						
			for stream in test_streams:
				stream = self.cleanTheStream(stream)
				print (self.calculateScore(stream))
			print ('done done')
				
		def removeExclamations(self, stream):
			print ('Removing all exclamation marks')
			index = 0
			while '!' in stream:
				if stream[index] == '!':
					stream.pop(index)
					stream.pop(index)
				else:
					index+=1
				
			return stream
		
		def removeGarbage(self, stream):
			print ('Removing all garbage')
			garbage_counter = 0
			index = 0
			while index < len(stream):
				if stream[index] == '<':
					stream.pop(index)
					while stream[index] != '>':
						stream.pop(index)
						garbage_counter += 1
					if stream[index] == '>':
						stream.pop(index)
				index+=1
			print (garbage_counter)
			return stream
			
		def calculateScore(self, stream):
			print ('Calculating score')
			value_counter = 0
			left_counter = 0
			index = 0
			while index < len(stream):
				if stream[index] == '{':
					left_counter += 1
				elif stream[index] == ',':
					pass
				elif stream[index] == '}':
					value_counter += left_counter
					left_counter -= 1
				else: 
					print ('Nu blev det konstigt')
					raise ValueError
				index+=1
			return (value_counter)
			
		def cleanTheStream(self, stream):
			stream = self.removeExclamations(stream)
			#print (stream)
			stream = self.removeGarbage(stream)
			#print (stream)
			print ('Stream clean')
			return stream
		
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			stream = self.read_instructions('input17_9.txt')
			stream = self.cleanTheStream(stream)
			print (self.calculateScore(stream))
								
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
#		x.testStuffTwo()
		x.doStuff()
