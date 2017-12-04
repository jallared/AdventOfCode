import string

		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.passphrases = []
			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			for passphrases in input:
				phrase = passphrases.strip("\n").split(" ")
				#row = list(map(int, row))
				self.passphrases.append(phrase)
				
			input.close()

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input17_4_t.txt')
			self.checkPassphraseOne()

		def testStuffTwo(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input17_4_2_t.txt')
			self.checkPassphraseTwo()			
			
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_instructions('input17_4.txt')
			self.checkPassphraseOne()
			self.checkPassphraseTwo()
		def checkPassphraseOne(self):
			valid_passphrases = 0
			for passphrase in self.passphrases:
				if len(passphrase) == len(set(passphrase)):
					valid_passphrases+=1
					
			print (valid_passphrases)

		def checkPassphraseTwo(self):
			valid_passphrases = 0
			sorted_passphrases = []
			
			for passphrase in self.passphrases:
				sorted_passphrase = []
				for words in passphrase:
					sorted_passphrase.append(''.join(sorted(words)))
				sorted_passphrases.append(sorted_passphrase)
			for passphrase in sorted_passphrases:
				counted = 0
				for word in passphrase:
					if passphrase.count(word) > 1:
						counted = 1					
				if counted == 0:
					valid_passphrases+=1
				
			print (valid_passphrases)
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
		x.testStuffTwo()
		x.doStuff()
