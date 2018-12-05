import string
import copy
import sys 
		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.lengths = []
			self.starting_list = []
			self.skip_size = 0
			self.index = 0
			
		def read_instructions_one(self, file_name):
			input = open(file_name, 'r')
			for row in input:
				self.lengths = list(map(int, row.strip("\n").split(",")))
			input.close()
			for i in range(256):
				self.starting_list.append(i)
				
		
		def read_instructions_two(self, file_name):
			input = open(file_name, 'r')
			for row in input:
				for character in row.strip("\n"):
					self.lengths.append(ord(character))
			input.close()
			for i in range(256):
				self.starting_list.append(i)
			
			for k in [17, 31, 73, 47, 23]:
				self.lengths.append(k)
		

		def testStuffOne(self):
			self.clear()
			self.lengths = [3,4,1,5]
			self.starting_list = [0,1,2,3,4]
			print (self.starting_list, self.lengths)
			self.knotHash()
			print ('Talen: ', self.starting_list[0], self.starting_list[1], 'Vilket ger: ', self.starting_list[0]*self.starting_list[1])
		
		def doStuff(self):
			self.clear()
			self.read_instructions_one('input17_10.txt')
#			print (self.lengths)
			self.knotHash()
			print ('Talen: ', self.starting_list[0], self.starting_list[1], 'Vilket ger: ', self.starting_list[0]*self.starting_list[1])
		
		def knotHash(self):
			for length in self.lengths:
#				print ('tut')
				sublist = []
				for i in range(length):
					while (i+self.index) > (len(self.starting_list)-1):
#						print ('nu ar det stort')
						i -= len(self.starting_list)
					sublist.append(self.starting_list[i+self.index])
				sublist.reverse()
				for i in range(length):
					while (i+self.index) > (len(self.starting_list)-1):
#						print ('stort..')
						i -= len(self.starting_list)
					self.starting_list[i+self.index] = sublist.pop(0)
				self.index += length+self.skip_size 
				while self.index > len(self.starting_list)-1:
					self.index-= len(self.starting_list)
				self.skip_size+=1
				
		def doStuffTwo(self):
			self.clear()
			self.read_instructions_two('input17_10.txt')
#			self.read_instructions_two('input17_10K.txt')
			print ('input = ', self.lengths)
			print ('len = ', len(self.lengths))
			for i in range(64):
				self.knotHash()
			the_sparse_hash = copy.deepcopy(self.starting_list)
			print ('the_sparse_hash = ', the_sparse_hash)
			print ('len = ' , len(the_sparse_hash))
#			print (65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22)

			
#			the_dense_hash = []			
#			for i in range(16):
#				the_dense_hash.append(the_sparse_hash[0+16*i]^the_sparse_hash[1+16*i]^the_sparse_hash[2+16*i]^the_sparse_hash[3+16*i]^the_sparse_hash[4+16*i]^the_sparse_hash[5+16*i]^the_sparse_hash[6+16*i]^the_sparse_hash[7+16*i]^the_sparse_hash[8+16*i]^the_sparse_hash[9+16*i]^the_sparse_hash[10+16*i]^the_sparse_hash[11+16*i]^the_sparse_hash[12+16*i]^the_sparse_hash[13+16*i]^the_sparse_hash[14+16*i]^the_sparse_hash[15+16*i])
#			print ('The Dense Hash = ', the_dense_hash)
			the_dense_hash = self.doTheXor(the_sparse_hash)
			print ('the_dense_hash = ', the_dense_hash)
			print ('len = ', len(the_dense_hash))
			hexes = []

			for number in the_dense_hash:
				hexes.append(hex(number).split('x')[1])
#			print (hexes)
			for i in range(len(hexes)):
				if len(hexes[i])==1:
					print (hexes[i])
					hexes[i] = '0' + hexes[i]
					print (hexes[i])
				if len(hexes[i])==0:
					hexes[i] = hexes[i]+'00'

			resultat = ''
			for item in hexes:
				resultat+=item
			
			print (resultat)
			print (len(resultat))

		def doTheXor(self, the_sparse_hash, length=16):
			the_dense_hash = []
			for i in range(length):
				the_dense_hash.append(the_sparse_hash[0+16*i]^the_sparse_hash[1+16*i]^the_sparse_hash[2+16*i]^the_sparse_hash[3+16*i]^the_sparse_hash[4+16*i]^the_sparse_hash[5+16*i]^the_sparse_hash[6+16*i]^the_sparse_hash[7+16*i]^the_sparse_hash[8+16*i]^the_sparse_hash[9+16*i]^the_sparse_hash[10+16*i]^the_sparse_hash[11+16*i]^the_sparse_hash[12+16*i]^the_sparse_hash[13+16*i]^the_sparse_hash[14+16*i]^the_sparse_hash[15+16*i])
			return (the_dense_hash)


if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
#		x.testStuffTwo()
#		x.doStuff()
		x.doStuffTwo()
		#x.testXor()