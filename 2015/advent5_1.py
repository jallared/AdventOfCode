import string

class Mening:
	def __init__(self, mening, req1, req2):
		self.mening = mening.strip("\n")
		self.req1 = req1
		self.req2 = req2
		self.length = len(self.mening)
		
	def naughty_or_nice_ett(self):
		aeiou=0
		for num in range(0,self.length,1):
				
				if num < self.length-1:
					if self.mening[num] == self.mening[num+1]:
						self.req1 = True
				
					if self.mening[num] in 'aeiou':
						aeiou += 1
						if aeiou > 2:
							self.req2=True
							
	def naughty_or_nice_tva(self):
		aeiou=0
		for num in range(0,self.length,1):

			if num < self.length-2:
								
				if self.mening[num]+ self.mening[num+1] in self.mening[num+2:]:
					self.req1 = True
					
				if self.mening[num] == self.mening[num+2]:
					self.req2=True

class Advent:
	def __init__(self):
		self.nice_counter=0
		self.naughty_counter=0
		self.nice = False
		self.input = open('input_5.txt', 'r')
		#self.femEtt()
		self.femTva()
		
	def naughty_or_nice(self):
		if self.nice:
			self.nice_counter += 1
		else:
			self.naughty_counter += 1
	
	def femTva(self):
		self.nice_counter = 0
		self.naughty_counter = 0
		
		
		for line in self.input:
			self.nice = False
			mening = Mening(line, False, False)
			mening.naughty_or_nice_tva()
					
		
			if mening.req1 == True and mening.req2 == True:
				self.nice = True
			
			self.naughty_or_nice()
	
		print 'naughty: ' + str(self.naughty_counter)
		print 'nice: ' + str(self.nice_counter)
	
	def femEtt(self):
		
		for line in self.input:
			self.nice = False
			mening = Mening(line, False, False)
			mening.naughty_or_nice_ett()
							
			if mening.req1 == True and mening.req2 == True:
				self.nice = True
				
			if 'ab' in mening.mening or 'cd' in mening.mening or 'pq' in mening.mening or 'xy' in mening.mening:
				self.nice = False
				
			self.naughty_or_nice()

		
		print 'naughty: ' + str(self.naughty_counter)
		print 'nice: ' + str(self.nice_counter)
		
if __name__ == "__main__":
	x = Advent()