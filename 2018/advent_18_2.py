import string

		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.box_id_list = []
			self.doubles = 0
			self.triples = 0
			
		def read_boxes(self, file_name):
			input = open(file_name, 'r')
			for instruction in input:
				variable = str(instruction.strip('\n'))
				self.box_id_list.append(variable)
			input.close()			

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			self.read_boxes('input_2_t.txt')
			for sequence in self.box_id_list:
				double, triple = self.check_box_id(sequence)
				if double:
					self.doubles += 1
				if triple:
					self.triples += 1
			
			print(self.doubles, self.triples, ' = ', self.doubles*self.triples)
		
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_boxes('input_2.txt')
			for sequence in self.box_id_list:
				double, triple = self.check_box_id(sequence)
				if double:
					self.doubles += 1
				if triple:
					self.triples += 1
			
			print(self.doubles, self.triples, ' = ', self.doubles*self.triples)

		def check_box_id(self, sequence):
			double, triple = False, False
			for letter in sequence:
				if self.find_double(letter, sequence):
					double = True
				if self.find_triple(letter, sequence):
					triple = True
						
			return (double, triple)
			
		def find_double(self, letter, sequence):
			if sequence.count(letter) == 2:
				return True
			else:
				return False

		def find_triple(self, letter, sequence):
			if sequence.count(letter) == 3:
				return True
			else:
				return False
			
		def testStuffTwo(self):
			self.clear()
			print ('Testing')
			self.read_boxes('input_2_2_t.txt')
			for index in range(0, len(self.box_id_list)):
				test, second_index = self.find_least_differing_characters(index)
				if test:
					print(self.box_id_list[index], self.box_id_list[second_index])
					break
		
		def find_least_differing_characters(self, index):
			sequence = self.box_id_list[index]
			temp_list = list(self.box_id_list)
			del temp_list[index]
			for box_id in temp_list:
#				print('loop 1')
				diff = 0
				for char_index in range(0, len(sequence)):
#					print('loop 2')
					if sequence[char_index] != box_id[char_index]:
						diff += 1
				if diff == 1:
					return True, self.box_id_list.index(box_id)
					
			return False, 0

		def doStuffTwo(self):
			self.clear()
			print ('Real stuff 2')
			self.read_boxes('input_2.txt')
			for index in range(0, len(self.box_id_list)):
				test, second_index = self.find_least_differing_characters(index)
				if test:
					box_1, box_2 = self.box_id_list[index], self.box_id_list[second_index]
					answer = ''
					for i in range(0, len(box_1)):
						if box_1[i] == box_2[i]:
							answer+=box_1[i]
					print(answer)
					break
					
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
		x.doStuff()
		x.testStuffTwo()
		x.doStuffTwo()