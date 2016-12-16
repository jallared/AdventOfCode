import string


class IP:
        def __init__(self):
                self.ip_addresses = []
                self.TLSsupportingaddresses = 0
                self.SSLsupportingaddresses = 0
                
        def clear(self):
                self.ip_addresses = []
                self.TLSsupportingaddresses = 0
                self.SSLsupportingaddresses = 0
                
        def readFile(self):
                input = open('input16_7.txt', 'r')
                for line in input:
                        self.ip_addresses.append(line)
                input.close()

        def readTestFile(self):
                self.ip_addresses = ['aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke', 'zazbz[bzb]cdb']
                                
        def count_IPv7(self):
                self.clear()
                self.readFile()

                for line in self.ip_addresses:
                        entire_string_contains_abba = False
                        substring_contains_abba = False
                        if self.find_abba(line):
                                entire_string_contains_abba = True
                                antal_hakparenteser = line.count('[')
                                if antal_hakparenteser > 0:
                                        for i in range(0, antal_hakparenteser):
                                                line = line.split('[',1)[1]
                                                substring, line = line.split(']',1)
                                                if self.find_abba(substring):
                                                        substring_contains_abba = True
                                else:
                                        print 'This should not happen!, muuuuuu'
                        else:
                                pass
                        if entire_string_contains_abba == True and substring_contains_abba == False:
                                self.TLSsupportingaddresses += 1
                        
                        
                print 'tot: ', self.TLSsupportingaddresses
        
        
        def find_abba(self, input_string):
                for i in range(0, len(input_string)-3):
                        if input_string[i] != input_string[i+1]:
                               if input_string[i] == input_string[i+3]:
                                       if input_string[i+1] == input_string[i+2]:
                                               return True
                return False

        def find_aba(self, input_strings):
                return_list = []
                for input_string in input_strings:
                        for i in range(0, len(input_string)-2):
                                if input_string[i] != input_string[i+1]:
                                        if input_string[i] == input_string[i+2]:
                                                return_list.append(input_string[i]+input_string[i+1]+input_string[i+2])
                return return_list

        def find_bab(self, input_strings, compare_string):
                for input_string in input_strings:
                        for i in range(0, len(input_string)-2):
                                if input_string[i]+input_string[i+1]+input_string[i+2] == compare_string[1]+compare_string[0]+compare_string[1]:
                                        return True
                return False

        def count_IP_SSL(self):
                self.clear()
                self.readFile()
                for line in self.ip_addresses:
                        aba_bab_found = False
                        antal_hakparenteser = line.count('[')
                        aba_candidates = []
                        bab_candidates = []
                        while antal_hakparenteser != 0:
                                aba_candidate, line = line.split('[',1)
                                aba_candidates.append(aba_candidate)
                                bab_candidate, line = line.split(']',1)
                                bab_candidates.append(bab_candidate)
                                antal_hakparenteser = line.count('[')
                        aba_candidates.append(line)
                        aba_list = self.find_aba(aba_candidates)
                        for aba in aba_list:
                                if self.find_bab(bab_candidates, aba):
                                        self.SSLsupportingaddresses += 1
                                        break
                        
                print self.SSLsupportingaddresses
                                                                
                        
                        

if __name__ == "__main__":
        x = IP()
        x.count_IPv7()
        x.count_IP_SSL()
