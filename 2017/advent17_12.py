import string
import copy
import sys 
		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.pipes = {}
			
		def read_instructions_one(self, file_name):
			input = open(file_name, 'r')
			for row in input:
				communicator, targets = row.strip("\n").split("<->")
				targets = targets.split(",")
				targets =  [int(i) for i in targets]
				communicator = int(communicator)
				#print (communicator, targets)
				self.pipes[communicator] = targets

		def testStuffOne(self):
			self.clear()
			self.read_instructions_one('input17_12_t.txt')
			self.investigatePipes()
			
		def doStuff(self):
			self.clear()
			self.read_instructions_one('input17_12.txt')
			self.investigatePipes()
			
		def investigatePipes(self):
			groups = []
			
			while len(self.pipes)>0:
				print ('tut')
				start_key = list(self.pipes.keys())[0]
				print ('tut', start_key)
#				start_point = self.pipes[start_key]
				#print ('tut', start_point)
				connected_pipes = [start_key]
				print ('tut', connected_pipes)
#				grouped_pipes = [0]
#				print (self.pipes[start_point])
				for pipe in self.pipes[start_key]:
					#print ('tyt', pipe)
					connected_pipes.append(pipe)
				del self.pipes[start_key]
				visited_pipes = [start_key]
			
				while len(connected_pipes) > 0:
					pipe = connected_pipes.pop()
					#print ('tut', pipe)
					if pipe not in visited_pipes:
						visited_pipes.append(pipe)
						connections = self.pipes[pipe]
						del self.pipes[pipe]
						for connection in connections:
							if connection not in visited_pipes:
								connected_pipes.append(connection)
				groups.append(visited_pipes)
			
					
			
			print (visited_pipes)
			print (len(visited_pipes))
			print (len(groups))
		
		
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
		x.doStuff()