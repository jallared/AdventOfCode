import string


class Advent:
	def __init__(self):
		self.wires = {}
		self.viewedkeys = []
		self.wires['a'] = {'value':None, 'solved':False}
		self.last_length = -1
		self.mainmetod()
			
	def mainmetod(self):
		input = open('input_7.txt', 'r')
		#input = open('input_7_test.txt', 'r')
		solved_rows = []
		while self.wires['a']['solved'] == False:
		#while len(solved_rows) < 9:
			print "Startar ny for-loop, har klarat ", len(solved_rows), " rader"
			print len(self.viewedkeys)
			input = open('input_7.txt', 'r')
			if self.last_length == len(solved_rows):
				print 'forra varvet gick vi igenom ', test, ' rader'
				break
			self.last_length = len(solved_rows)
			test = 0
			for row in input:
				test+=1
				if row in solved_rows:
					continue
				
				value,wire=row.split("->")
				wire = wire.strip(" ").strip("\n").strip("\r")
				self.viewedkeys = self.wires.viewkeys()
				
				#AND
				if 'AND' in value:
					var1, var2 = value.split("AND")
					try:
						var1 = int(var1)
						number_1 = True
					except:
						number_1 = False
						var1 = var1.strip(" ")
					try:
						var2 = int(var2)
						number_2 = True
					except:
						var2 = var2.strip(" ")
						number_2 = False
					if number_1 == number_2 == False:	
						if var1 in self.viewedkeys and var2 in self.viewedkeys:
							if self.wires[var1]['solved'] == True and self.wires[var2]['solved'] == True:
								self.wires[wire] = {'value':self.AND(self.wires[var1]['value'], self.wires[var2]['value']), 'solved':True}
								solved_rows.append(row)
							else:
								self.wires[wire] = {'value':None, 'solved':False}
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					elif number_1 == False and number_2 == True:
						if var1 in self.viewedkeys:
							if self.wires[var1]['solved'] == True:
								self.wires[wire] = {'value':self.AND(self.wires[var1]['value'], var2), 'solved':True}
								solved_rows.append(row)
							else:
								self.wires[wire] = {'value':None, 'solved':False}
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					elif number_1 == True and number_2 == False:
						if var2 in self.viewedkeys:
							if self.wires[var2]['solved'] == True:
								self.wires[wire] = {'value':self.AND(self.wires[var2]['value'], var1), 'solved':True}
								solved_rows.append(row)
							else:
								self.wires[wire] = {'value':None, 'solved':False}
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					
				#LSHIFT
				elif 'LSHIFT' in value:
					variable, amount = value.split("LSHIFT")
					variable = variable.strip(" ")
					amount = int(amount)
									
					if variable in self.viewedkeys:
						if self.wires[variable]['solved'] == True:
							self.wires[wire] = {'value':self.LSHIFT(self.wires[variable]['value'], amount), 'solved':True}
							solved_rows.append(row)
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					else:
						self.wires[wire] = {'value':None, 'solved':False}
					
				#RSHIFT
				elif 'RSHIFT' in value:
					variable, amount = value.split("RSHIFT")
					variable = variable.strip(" ")
					amount = int(amount)
									
					if variable in self.viewedkeys:
						if self.wires[variable]['solved'] == True:
							self.wires[wire] = {'value':self.RSHIFT(self.wires[variable]['value'], amount), 'solved':True}
							solved_rows.append(row)
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					else:
						self.wires[wire] = {'value':None, 'solved':False}
						
				#OR
				elif 'OR' in value:
					var1, var2 = value.split("OR")
					var1 = var1.strip(" ")
					var2 = var2.strip(" ")
					if var1 in self.viewedkeys and var2 in self.viewedkeys:
						if self.wires[var1]['solved'] == True and self.wires[var2]['solved'] == True:
							self.wires[wire] = {'value':self.OR(self.wires[var1]['value'], self.wires[var2]['value']), 'solved':True}
							solved_rows.append(row)
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					else:
						self.wires[wire] = {'value':None, 'solved':False}
					
				#NOT
				elif 'NOT' in value:
					instruction, variable,trash = value.split(" ")
					if variable in self.viewedkeys:
						if self.wires[variable]['solved'] == True:
							self.wires[wire] = {'value':self.NOT(self.wires[variable]['value']), 'solved':True}
							solved_rows.append(row)
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					else:
						self.wires[wire] = {'value':None, 'solved':False}
						
				#APPEND
				else:
					try:
						value = int(value)
						self.wires[wire] = {'value':value, 'solved':True}
						solved_rows.append(row)
					except:
						value = value.strip(" ")
						if value in self.viewedkeys:
							if self.wires[value]['solved'] == True:
								self.wires[wire] = {'value':self.wires[value]['value'], 'solved':True}
								solved_rows.append(row)
							else:
								self.wires[wire] = {'value':None, 'solved':False}
						else:
							self.wires[wire] = {'value':None, 'solved':False}
		
		siffra=0
		for sak in self.wires:
			print sak, self.wires[sak]
			if self.wires[sak]['solved'] == True:
				siffra+=1
		print siffra
		solved_rows = []
		temp = self.wires['a']['value']
		self.wires =  {}
		self.viewedkeys = []
		self.wires['a'] = {'value':None, 'solved':False}
		self.last_length = -1
		self.wires['b'] = {'value':temp, 'solved':True}
		
		while self.wires['a']['solved'] == False:
		#while len(solved_rows) < 9:
			print "Startar ny for-loop, har klarat ", len(solved_rows), " rader"
			print len(self.viewedkeys)
			input = open('input_7.txt', 'r')
			if self.last_length == len(solved_rows):
				print 'forra varvet gick vi igenom ', test, ' rader'
				break
			self.last_length = len(solved_rows)
			test = 0
			for row in input:
				test+=1
				if row in solved_rows:
					continue
				
				value,wire=row.split("->")
				wire = wire.strip(" ").strip("\n").strip("\r")
				if wire == 'b':
					continue
				self.viewedkeys = self.wires.viewkeys()
				
				#AND
				if 'AND' in value:
					var1, var2 = value.split("AND")
					try:
						var1 = int(var1)
						number_1 = True
					except:
						number_1 = False
						var1 = var1.strip(" ")
					try:
						var2 = int(var2)
						number_2 = True
					except:
						var2 = var2.strip(" ")
						number_2 = False
					if number_1 == number_2 == False:	
						if var1 in self.viewedkeys and var2 in self.viewedkeys:
							if self.wires[var1]['solved'] == True and self.wires[var2]['solved'] == True:
								self.wires[wire] = {'value':self.AND(self.wires[var1]['value'], self.wires[var2]['value']), 'solved':True}
								solved_rows.append(row)
							else:
								self.wires[wire] = {'value':None, 'solved':False}
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					elif number_1 == False and number_2 == True:
						if var1 in self.viewedkeys:
							if self.wires[var1]['solved'] == True:
								self.wires[wire] = {'value':self.AND(self.wires[var1]['value'], var2), 'solved':True}
								solved_rows.append(row)
							else:
								self.wires[wire] = {'value':None, 'solved':False}
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					elif number_1 == True and number_2 == False:
						if var2 in self.viewedkeys:
							if self.wires[var2]['solved'] == True:
								self.wires[wire] = {'value':self.AND(self.wires[var2]['value'], var1), 'solved':True}
								solved_rows.append(row)
							else:
								self.wires[wire] = {'value':None, 'solved':False}
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					
				#LSHIFT
				elif 'LSHIFT' in value:
					variable, amount = value.split("LSHIFT")
					variable = variable.strip(" ")
					amount = int(amount)
									
					if variable in self.viewedkeys:
						if self.wires[variable]['solved'] == True:
							self.wires[wire] = {'value':self.LSHIFT(self.wires[variable]['value'], amount), 'solved':True}
							solved_rows.append(row)
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					else:
						self.wires[wire] = {'value':None, 'solved':False}
					
				#RSHIFT
				elif 'RSHIFT' in value:
					variable, amount = value.split("RSHIFT")
					variable = variable.strip(" ")
					amount = int(amount)
									
					if variable in self.viewedkeys:
						if self.wires[variable]['solved'] == True:
							self.wires[wire] = {'value':self.RSHIFT(self.wires[variable]['value'], amount), 'solved':True}
							solved_rows.append(row)
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					else:
						self.wires[wire] = {'value':None, 'solved':False}
						
				#OR
				elif 'OR' in value:
					var1, var2 = value.split("OR")
					var1 = var1.strip(" ")
					var2 = var2.strip(" ")
					if var1 in self.viewedkeys and var2 in self.viewedkeys:
						if self.wires[var1]['solved'] == True and self.wires[var2]['solved'] == True:
							self.wires[wire] = {'value':self.OR(self.wires[var1]['value'], self.wires[var2]['value']), 'solved':True}
							solved_rows.append(row)
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					else:
						self.wires[wire] = {'value':None, 'solved':False}
					
				#NOT
				elif 'NOT' in value:
					instruction, variable,trash = value.split(" ")
					if variable in self.viewedkeys:
						if self.wires[variable]['solved'] == True:
							self.wires[wire] = {'value':self.NOT(self.wires[variable]['value']), 'solved':True}
							solved_rows.append(row)
						else:
							self.wires[wire] = {'value':None, 'solved':False}
					else:
						self.wires[wire] = {'value':None, 'solved':False}
						
				#APPEND
				else:
					try:
						value = int(value)
						self.wires[wire] = {'value':value, 'solved':True}
						solved_rows.append(row)
					except:
						value = value.strip(" ")
						if value in self.viewedkeys:
							if self.wires[value]['solved'] == True:
								self.wires[wire] = {'value':self.wires[value]['value'], 'solved':True}
								solved_rows.append(row)
							else:
								self.wires[wire] = {'value':None, 'solved':False}
						else:
							self.wires[wire] = {'value':None, 'solved':False}
		
		siffra=0
		for sak in self.wires:
			print sak, self.wires[sak]
			if self.wires[sak]['solved'] == True:
				siffra+=1
		print siffra
		
	def OR(self, var1, var2):
		return (var1|var2 & 0xffff)
		
	def AND(self, var1, var2):
		return (var1 & var2 & 0xffff)
			
	def LSHIFT(self, var, amount):
		return (var<<amount & 0xffff)
			
	def RSHIFT(self, var, amount):
		return (var >> amount & 0xffff)
			
	def NOT(self, var):
		return (~var & 0xffff)
		
		
if __name__ == "__main__":
	x = Advent()