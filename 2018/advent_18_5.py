import string

		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.polymer = ''
			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			for instruction in input:
				self.polymer = str(instruction.strip('\n'))
			input.close()			

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input_5_t.txt')
			
			start_length = len(self.polymer)
			new_length = 0
			while new_length < start_length:
				start_length = len(self.polymer)
				self.remove_pairs()
				
				new_length = len(self.polymer)
				
			print(len(self.polymer))

		def testStuffTwo(self):
			print ('Testing')
			lengths = {}
			for letter in 'abcdefghijklmnopqrstuvwxyz':
				self.clear()
				self.read_instructions('input_5_t.txt')
				self.polymer = self.polymer.replace(letter, '')
				self.polymer = self.polymer.replace(letter.upper(), '')
				
				
				start_length = len(self.polymer)
				new_length = 0
				while new_length < start_length:
					start_length = len(self.polymer)
					self.remove_pairs()
					
					new_length = len(self.polymer)
				
				lengths[letter] = len(self.polymer)
			
			minimum = min(lengths, key=lengths.get)
			print(minimum, ' ', lengths[minimum])
			
		
		def remove_pairs(self):
			self.polymer = self.polymer.replace('aA', '')
			self.polymer = self.polymer.replace('Aa', '')
			self.polymer = self.polymer.replace('bB', '')
			self.polymer = self.polymer.replace('Bb', '')
			self.polymer = self.polymer.replace('cC', '')
			self.polymer = self.polymer.replace('Cc', '')
			self.polymer = self.polymer.replace('dD', '')
			self.polymer = self.polymer.replace('Dd', '')
			self.polymer = self.polymer.replace('eE', '')
			self.polymer = self.polymer.replace('Ee', '')
			self.polymer = self.polymer.replace('fF', '')
			self.polymer = self.polymer.replace('Ff', '')
			self.polymer = self.polymer.replace('gG', '')
			self.polymer = self.polymer.replace('Gg', '')
			self.polymer = self.polymer.replace('hH', '')
			self.polymer = self.polymer.replace('Hh', '')
			self.polymer = self.polymer.replace('iI', '')
			self.polymer = self.polymer.replace('Ii', '')
			self.polymer = self.polymer.replace('jJ', '')
			self.polymer = self.polymer.replace('Jj', '')
			self.polymer = self.polymer.replace('kK', '')
			self.polymer = self.polymer.replace('Kk', '')
			self.polymer = self.polymer.replace('lL', '')
			self.polymer = self.polymer.replace('Ll', '')
			self.polymer = self.polymer.replace('mM', '')
			self.polymer = self.polymer.replace('Mm', '')
			self.polymer = self.polymer.replace('nN', '')
			self.polymer = self.polymer.replace('Nn', '')
			self.polymer = self.polymer.replace('oO', '')
			self.polymer = self.polymer.replace('Oo', '')
			self.polymer = self.polymer.replace('pP', '')
			self.polymer = self.polymer.replace('Pp', '')
			self.polymer = self.polymer.replace('qQ', '')
			self.polymer = self.polymer.replace('Qq', '')
			self.polymer = self.polymer.replace('rR', '')
			self.polymer = self.polymer.replace('Rr', '')
			self.polymer = self.polymer.replace('sS', '')
			self.polymer = self.polymer.replace('Ss', '')
			self.polymer = self.polymer.replace('tT', '')
			self.polymer = self.polymer.replace('Tt', '')
			self.polymer = self.polymer.replace('uU', '')
			self.polymer = self.polymer.replace('Uu', '')
			self.polymer = self.polymer.replace('vV', '')
			self.polymer = self.polymer.replace('Vv', '')
			self.polymer = self.polymer.replace('wW', '')
			self.polymer = self.polymer.replace('Ww', '')
			self.polymer = self.polymer.replace('xX', '')
			self.polymer = self.polymer.replace('Xx', '')
			self.polymer = self.polymer.replace('yY', '')
			self.polymer = self.polymer.replace('Yy', '')
			self.polymer = self.polymer.replace('zZ', '')
			self.polymer = self.polymer.replace('Zz', '')
					
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_instructions('input_5.txt')
			start_length = len(self.polymer)
			new_length = 0
			while new_length < start_length:
				start_length = len(self.polymer)
				self.remove_pairs()
				
				new_length = len(self.polymer)
				
			print(len(self.polymer))
		
		def doStuffTwo(self):
			print ('Real stuff')
			lengths = {}
			for letter in 'abcdefghijklmnopqrstuvwxyz':
				self.clear()
				self.read_instructions('input_5.txt')
				self.polymer = self.polymer.replace(letter, '')
				self.polymer = self.polymer.replace(letter.upper(), '')
				
				
				start_length = len(self.polymer)
				new_length = 0
				while new_length < start_length:
					start_length = len(self.polymer)
					self.remove_pairs()
					
					new_length = len(self.polymer)
				
				lengths[letter] = len(self.polymer)
			
			minimum = min(lengths, key=lengths.get)
			print(minimum, ' ', lengths[minimum])
	
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
		x.doStuff()
		x.testStuffTwo()
		x.doStuffTwo()