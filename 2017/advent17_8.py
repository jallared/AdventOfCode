import string
import copy
import sys 
		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.registers = {}
			self.instructions = []
			self.maximum_register_value = 0
	
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			
			for row in input:
				self.instructions.append(row.strip("\n"))
			input.close()

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input17_8_t.txt')
			self.calculateRegisters()
		
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_instructions('input17_8.txt')
			self.calculateRegisters()
			
		def calculateRegisters(self):
			print (self.instructions)
			
			for instruction in self.instructions:
				instr, cond = self.decodeInstruction(instruction)
				
				if self.evaluateCondition(cond):
					self.performInstruction(instr)
				maximi = self.registers[max(self.registers, key=self.registers.get)]
				if maximi > self.maximum_register_value:
					self.maximum_register_value = maximi
			print ('Hela registret: ', self.registers)
			print ('Max: ', self.registers[max(self.registers, key=self.registers.get)])
			print ('Max ever: ', self.maximum_register_value)
			
		def decodeInstruction(self, instruction):
			(instruction, condition) = instruction.split("if")
			return (instruction, condition.lstrip(" "))

		def performInstruction(self, instruction):
			register, instruction, value = (instruction.rstrip(" ").split(" "))
			value = int(value)
			if instruction == 'inc':
				self.increaseValue(value, register)
			elif instruction == 'dec':
				self.decreaseValue(value, register)
			else:
				raise ValueError
				
		def increaseValue(self, value, register):
			try: 
				self.registers[register]+=value
			except:
				self.registers[register]=value
			
		def decreaseValue(self, value, register):
			
			try: 
				self.registers[register]-= value
			except:
				self.registers[register] = -value
		
		def evaluateCondition(self, condition):
			(condition_register, operator, value) = condition.split(" ")
			value = int(value)
#			print (condition)
#			print (condition_register, operator, value)
#			raise ValueError
			try:
				condition_register_value = int(self.registers[condition_register])
			except:
				self.registers[condition_register] = 0
				condition_register_value = int(self.registers[condition_register])
			
			print ('hej, evaluate: ', condition_register_value, value)
			if operator == '<':
				if condition_register_value < value:
					return True
			elif operator == '>':
				if condition_register_value > value:
					return True
			elif operator == '==':
				if condition_register_value == value:
					return True
			elif operator == '!=':
				if condition_register_value != value:
					return True
			elif operator == '<=':
				if condition_register_value <= value:
					return True
			elif operator == '>=':
				if condition_register_value >= value:
					return True
			
			else:
				raise ValueError
			
			return False
		
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
#		x.testStuffTwo()
		x.doStuff()
