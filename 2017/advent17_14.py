import string
import copy
import sys 
import advent17_10
		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.grid = []
		
		
		def clearKnot(self):
			self.lengths = []
			self.starting_list = []
			self.skip_size = 0
			self.index = 0	
			
		def calculateKnotHash(self, input):
			self.clearKnot()
			
			for character in input:
				self.lengths.append(ord(character))

			for i in range(256):
				self.starting_list.append(i)
			
			for k in [17, 31, 73, 47, 23]:
				self.lengths.append(k)
			for i in range(64):
				self.knotHash()
			the_sparse_hash = copy.deepcopy(self.starting_list)

			the_dense_hash = self.doTheXor(the_sparse_hash)

			hexes = []

			for number in the_dense_hash:
				hexes.append(hex(number).split('x')[1])
	
			for i in range(len(hexes)):
				if len(hexes[i])==1:
					hexes[i] = '0'+ hexes[i]
			
			resultat = ''
			for item in hexes:
				resultat+=item
			
			return resultat
		
		def knotHash(self):
			for length in self.lengths:
				sublist = []
				for i in range(length):
					while (i+self.index) > (len(self.starting_list)-1):
						i -= len(self.starting_list)
					sublist.append(self.starting_list[i+self.index])
				sublist.reverse()
				for i in range(length):
					while (i+self.index) > (len(self.starting_list)-1):
						i -= len(self.starting_list)
					self.starting_list[i+self.index] = sublist.pop(0)
				self.index += length+self.skip_size 
				while self.index > len(self.starting_list)-1:
					self.index-= len(self.starting_list)
				self.skip_size+=1
		
		def doTheXor(self, the_sparse_hash, length=16):
			the_dense_hash = []
			for i in range(length):
				the_dense_hash.append(the_sparse_hash[0+16*i]^the_sparse_hash[1+16*i]^the_sparse_hash[2+16*i]^the_sparse_hash[3+16*i]^the_sparse_hash[4+16*i]^the_sparse_hash[5+16*i]^the_sparse_hash[6+16*i]^the_sparse_hash[7+16*i]^the_sparse_hash[8+16*i]^the_sparse_hash[9+16*i]^the_sparse_hash[10+16*i]^the_sparse_hash[11+16*i]^the_sparse_hash[12+16*i]^the_sparse_hash[13+16*i]^the_sparse_hash[14+16*i]^the_sparse_hash[15+16*i])
			return (the_dense_hash)
			
			


			
		def testStuffOne(self):
			self.clear()
			self.input_string = 'flqrgnkx'
			self.doHashStuff(8)
			self.clear()
			self.input_string = 'flqrgnkx'
			self.doHashStuff(128)
			
		def doStuff(self):
			self.clear()
			self.input_string = 'hwlqcszp'
			grid = self.doHashStuff(128)
		
		def doStuffTwo(self):
			self.clear()
			self.input_string = 'hwlqcszp'
			grid = self.doHashStuff(128)
		
		def doHashStuff(self, grid_length):
			
			for i in range(grid_length):
				temp = self.input_string + '-' + str(i)
				self.grid.append(self.calculateKnotHash(temp))
			
			temp = []
			for hash in self.grid:
				test = ''
				for character in hash:
					apa = bin(int(character, 16)).split('0b')[1]
					while (len(apa) < 4):
						apa = '0'+ apa
					test+=apa

					
				temp.append(test)
				
			tmp = []
			resultat=0
			for item in temp:
				subtmp = ''
				for test in item:
					if test == '1':
						resultat+=1
						subtmp+='#'
					elif test == '0':
						subtmp+='.'
					else:
						raise ValueError
				tmp.append(subtmp)
										
			print (resultat)
			return tmp
			

		
		
		
		
		
		
if __name__ == "__main__":
		x = Stuff()
		#x.testStuffOne()
		x.doStuff()