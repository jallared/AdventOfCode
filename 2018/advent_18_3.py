import string
from collections import defaultdict
		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.claim_list = []
			self.data = open('input_3.txt').read().splitlines()

			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			for line in input:
				variable = str(line.strip('\n'))
				number, instruction = variable.split("@")
				number = number.strip("#")
				number = int(number)
				coordinates, size = instruction.split(":")
				coordinates = coordinates.strip(" ")
				size = size.strip(" ")
				x_coordinate, y_coordinate = coordinates.split(",")
				width, height = size.split("x")
				x_coordinate = int(x_coordinate)
				y_coordinate = int(y_coordinate)
				width = int(width)
				height = int(height)
				self.claim_list.append((number, x_coordinate, y_coordinate, width, height))
			input.close()			

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input_3_t.txt')
			overlap = defaultdict(int)
			for claim in self.claim_list:
				number, x_coordinate, y_coordinate, width, height = claim

				for w in range(width):
					for h in range(height):
						overlap[(x_coordinate+w, y_coordinate+h)] += 1

			overlaps = 0
			for value in overlap.values():
				if value > 1:
					overlaps += 1
			
			print(overlaps)
			overlapping_claims = set()
			all_claims = set()
			
			for claim in self.claim_list:
				number, x_coordinate, y_coordinate, width, height = claim
				all_claims.add(number)
				for w in range(width):
					for h in range(height):
						xy = (x_coordinate+w, y_coordinate+h)
						if overlap[xy] > 1:
							overlapping_claims.add(number)
			print(all_claims-overlapping_claims)
			
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_instructions('input_3.txt')
			overlap = defaultdict(int)
			
			for claim in self.claim_list:
				number, x_coordinate, y_coordinate, width, height = claim

				for w in range(width):
					for h in range(height):
						overlap[(x_coordinate+w, y_coordinate+h)] += 1
						
			overlaps = 0
			for value in overlap.values():
				if value > 1:
					overlaps += 1
			
			print(overlaps)
			
			print("Part 2")
			
			overlapping_claims = set()
			all_claims = set()
			
			for claim in self.claim_list:
				number, x_coordinate, y_coordinate, width, height = claim
				all_claims.add(number)
				for w in range(width):
					for h in range(height):
						xy = (x_coordinate+w, y_coordinate+h)
						if overlap[xy] > 1:
							overlapping_claims.add(number)
			print(all_claims-overlapping_claims)
								

if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
		x.doStuff()
	