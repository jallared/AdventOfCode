import string
import copy
import sys 
		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.firewall = {}
			self.firewall_length = 0
			self.position = -1
			self.severity = 0
			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			for row in input:
				depth, range_ = list(map(int, row.strip("\n").strip(" ").split(":")))
				self.firewall[depth] = (range_, 0, 1)
			self.firewall_length = max(self.firewall, key=int)
			for i in range(self.firewall_length):
				if i not in self.firewall:
					self.firewall[i] = (0, -1, 0)
			
			self.setFirewall()
		
		def setFirewall(self):
			self.temp_firewall = copy.deepcopy(self.firewall)
			self.temp_firewall_length = copy.deepcopy(self.firewall_length)
			
		def resetFirewall(self):
			self.firewall = copy.deepcopy(self.temp_firewall)
			self.firewall_length = copy.deepcopy(self.temp_firewall_length)
			self.position = -1
			self.severity = 0

		def testStuffOne(self):
			self.clear()
			self.read_instructions('input17_13_t.txt')
			self.traverseFirewall()	
			print (self.severity)
			
		def doStuff(self):
			self.clear()
			self.read_instructions('input17_13.txt')
			self.traverseFirewall()	
			print (self.severity)
		
		def doStuffTwo(self):
			solution_found = False
			self.clear()
			self.read_instructions('input17_13.txt')
			t=0
			while solution_found == False:
				self.resetFirewall()
				t+=1
				self.moveScanners()
				self.setFirewall()
#				print ('Waited ', t, ' = ', k, ' picoseconds')
				solution_found = self.traverseFirewallTwo()
				#if (t % 1000) == 0:
				#	print (t)
				#print (t)
			print (t, ' klarade biffen')
		
		def doStuffTwoTest(self):
			solution_found = False
			self.clear()
			self.read_instructions('input17_13_t.txt')
			t=0
			while solution_found == False:
				self.resetFirewall()
				t+=1
				self.moveScanners()
				self.setFirewall()
#				print ('Waited ', t, ' = ', k, ' picoseconds')
				solution_found = self.traverseFirewallTwo()
				if (t % 1000) == 0:
					print (t)
				#print (t)
			print (t, ' klarade biffen')
			
		def traverseFirewall(self):
			while self.position < self.firewall_length:				
				#print ('move time')
				self.moveMe()
				self.checkScanResult()
				self.moveScanners()
			
		def moveMe(self):
			self.position+=1
		
		def checkScanResult(self):
			#try: 
			range, scan_position, direction = self.firewall[self.position]
			#except:
				#print ('ingen här, ', self.position)
				#scan_position = -1
			
			if scan_position == 0:
				#print ('AJ AJ, ', self.position)
				self.severity += (range*self.position)
				
			#print ('if Scanner position == my position, severity += depth*range')
			
		def moveScanners(self):
			for key in self.firewall:
				range, scan_position, direction = self.firewall[key]
				
				if direction == 1:
					if scan_position < range-1:
						scan_position+=direction
					elif scan_position == range-1:
						direction = -1
						scan_position+=direction
				elif direction == -1:
					if scan_position > 0:
						scan_position+=direction
					elif scan_position == 0:
						direction = 1
						scan_position+=direction
				self.firewall[key] = (range, scan_position, direction)
				
				
		def traverseFirewallTwo(self):
			while self.position < self.firewall_length:				
				#print ('move time')
				self.moveMe()
				resultat = self.checkScanResultTwo()
				if not resultat:
					return False
				self.moveScanners()
				
				
		def checkScanResultTwo(self):
			#try: 
			range, scan_position, direction = self.firewall[self.position]
			#except:
				#print ('ingen här, ', self.position)
			#	scan_position = -1
			
			if scan_position == 0:
#				print ('AJ AJ, ', self.position)
				return False
				#self.severity += (range*self.position)
			return True
			#print ('if Scanner position == my position, severity += depth*range')		
		
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
		x.doStuff()
		x.doStuffTwoTest()
		x.doStuffTwo()
		print ('3873662 är rätt svar')