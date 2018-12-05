import string
import copy
import sys 
		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.left_hand_side = []
			self.right_hand_side = []
			self.items = []
			self.parabol_list = []
			self.parents = []
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			
			for row in input:
				if "->" in row:
					[left, right] = row.split("->")
					[left_name, weight, throwaway] = left.split(" ")
					self.left_hand_side.append(left_name)
					self.parents.append(left_name)
					temp = []
					for item in right.split(", "):
						item = item.strip("\n").strip(" ")
						self.right_hand_side.append(item)
						temp.append(item)
					self.parabol_list.append((left_name, temp))
				else:
					[left_name, weight] = row.split(" ")
				weight = int(weight.strip("(").strip("\n").strip(")"))
				self.items.append((left_name, weight))
								
			input.close()

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input17_7_t.txt')
			self.findBase()
		
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_instructions('input17_7.txt')
			self.findBase()
			
		def findBase(self):
			names = []
#			print (len(self.left_hand_side), len(self.right_hand_side))
			index = 0
			while len(self.left_hand_side) > 1:
				try:
					name = self.left_hand_side[index]
					self.right_hand_side.index(name)
					self.left_hand_side.pop(index)	
					index = 0
				except IndexError as err:
					index+=1
					if index > len(self.left_hand_side)-1:
						index = 0
#					print("Index error: {0}".format(err))
				except ValueError as err:
					index+=1
					if index > len(self.left_hand_side)-1:
						index = 0
#					print("Value error: {0}".format(err))

			print (self.left_hand_side)
		
		def Karro(self):
			self.clear()
			print ('Karro')
			self.read_instructions('input17_7.txt')
			root = 'veboyvy'
			print ('Efter klar loopande, hitta varde for den felande variabeln och justera den...')
			self.testLoop(root)

		def testKarro(self):
			self.clear()
			print ('Testing Karro')
			self.read_instructions('input17_7_t.txt')
			root = 'tknk'
			self.testLoop(root)
		
		def testLoop(self, name):
			vikter = []
			for index in range(len(self.parabol_list)):
				(parent, children) = self.parabol_list[index]
				if parent == name:
					for child in children:
						vikter.append(self.calculate(child))
					for vikt in vikter:
						#print (vikt)
						if vikt != vikter[0]:
							print ('Parent = ', parent)
							print ('Children = ', children)
							print ('Weights = ', vikter)
							raise Exception
			
			
		def calculate(self, child):
			if child not in self.parents:
				return self.findWeight(child)
			else:
				for index in range(len(self.parabol_list)):
					(parent, children) = self.parabol_list[index]
					#print ('tut')
					if parent == child:
						#print ('hest')
						weights = []
						for barn in children:
							weights.append(self.calculate(barn))
						for weight in weights:
							#print (weight)
							if weight != weights[0]:
								print ('Parent = ', parent)
								print ('Children = ', children)
								print ('Weights = ', weights)
								raise Exception
						returnWeight = self.findWeight(parent)
						for weight in weights:
							returnWeight+=weight
						#print (returnWeight)
						return returnWeight
				
		def findWeight(self, name):
			for index in range(len(self.items)):
				if name == self.items[index][0]:
					weight = self.items[index][1]
					#print (weight)
					return (weight)

		
		
		
		#starta i botten
		#loopa över alla barn
		#för alla barn: kolla om alla barn är lika (rekursivt)
		#när man kommer till ett löv, returnera värde
		#Om inte alla barn är samma, skriv ut vilken nod det är, och vilka värden alla barn har
		#Om alla är lika, returnera summan av alla barn + själv
		
		
		#Del 2:
		# Tupler med namn och vikt for alla
		# Kontrollera att alla på samma högersida har samma vikt
		# Identifiera vilken som diffar och se vilka vikter de pa den sidan har
			
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
#		x.testStuffTwo()
		x.doStuff()
#		x.testStuff()
#		x.testKarro()
		x.Karro()