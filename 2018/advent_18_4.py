import string
from collections import defaultdict
		
class Stuff:
		def __init__(self):
			self.clear()
		
		def clear(self):
			self.guard_log = []
			self.guard_result = defaultdict(int)
			self.guard_sleeping_total = defaultdict(int)
			
			
		def read_instructions(self, file_name):
			input = open(file_name, 'r')
			for line in input:
				timestamp, event = line.strip("\n")[1:].split(']')
				event = event.strip()
				self.guard_log.append((timestamp, event))
			input.close()
			self.guard_log.sort(key=lambda tup: tup[0])
			

		def testStuffOne(self):
			self.clear()
			print ('Testing')
			self.read_instructions('input_4_t.txt')
			while len(self.guard_log)>0:
				interpreted_log = self.interpret_log()
				self.log_guards(interpreted_log)
			
			self.find_best_guard_part_one()
			self.find_best_guard_part_two()
			
		def interpret_log(self):
			temp = []
			if self.guard_log[0][1][:5] == 'Guard':
				temp.append(self.guard_log.pop(0))
				while True:
					try:
						if self.guard_log[0][1][:5] != 'Guard':
							temp.append(self.guard_log.pop(0))
						else:
							return temp
					except:
						return temp

		def log_guards(self, interpreted_log):
			
			guard_identifier = interpreted_log.pop(0)[1].split(" ")
			guard_number = int(guard_identifier[1][1:])
			starting_minute = 0
			guard_state = 'awake'
			for timestamp, observation in interpreted_log:
				minute = int(timestamp.split(" ")[1].split(":")[1])
				
				if guard_state == 'awake':
					starting_minute = minute
					guard_state = 'sleeping'
					
				elif guard_state == 'sleeping': 	
					for m in range(starting_minute, minute):
						self.guard_result[(guard_number, m)] += 1
						self.guard_sleeping_total[guard_number] += 1
							
					guard_state = 'awake'
					starting_minute = minute
				
			
		
		def doStuff(self):
			self.clear()
			print ('Real stuff')
			self.read_instructions('input_4.txt')
			while len(self.guard_log)>0:
				interpreted_log = self.interpret_log()
				self.log_guards(interpreted_log)
				
			self.find_best_guard_part_one()
			self.find_best_guard_part_two()
			
		def find_best_guard_part_one(self):
			best_guard = max(self.guard_sleeping_total, key=self.guard_sleeping_total.get)
			
			most_sleep = 0
			best_minute = -1
			for i in range(0, 59):
				result = self.guard_result[(best_guard, i)]
				if  result > most_sleep:
					most_sleep = result
					best_minute = i
			
			print(best_guard, best_minute, best_guard*best_minute)
			
		def find_best_guard_part_two(self):
			best_guard, minute = max(self.guard_result, key=self.guard_result.get)
			print(best_guard, minute, best_guard*minute)
			
if __name__ == "__main__":
		x = Stuff()
		x.testStuffOne()
		x.doStuff()
