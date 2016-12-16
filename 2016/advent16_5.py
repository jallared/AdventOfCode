import string
import md5


class Chess:
        def __init__(self):
                self.chess_input = 'abbhdwsy'
                #self.chess_input = 'abc'
                self.password = ''
                self.password_two = ["","","","","","","",""]
                self.password_index = ['0','1','2','3','4','5','6','7']
                self.used_indexes = []
                
                
        def doStuff(self):
                answer = 0
                #first_six_digits = '111111'
                for i in range(0,8):
                        first_six_digits = '111111'
                        while first_six_digits[:-1] != '00000':
                                answer += 1
                                kod = md5.new()
                                kod.update(self.chess_input)
                                kod.update(str(answer))
                                first_six_digits = kod.hexdigest()
                                first_six_digits = first_six_digits[0] + first_six_digits[1] + first_six_digits[2] + first_six_digits[3] +first_six_digits[4] + first_six_digits[5]
                        self.password += first_six_digits[-1]
                        
                print self.password

        def doStuffTwo(self):
                answer = 0
                good_indexes = 0
                while len(self.used_indexes) < 8:
                        first_seven_digits = '1111111'
                        while first_seven_digits[:-2] != '00000':
                                answer += 1
                                kod = md5.new()
                                kod.update(self.chess_input)
                                kod.update(str(answer))
                                first_seven_digits = kod.hexdigest()
                                first_seven_digits = first_seven_digits[0] + first_seven_digits[1] + first_seven_digits[2] + first_seven_digits[3] +first_seven_digits[4] + first_seven_digits[5] + first_seven_digits[6]
                        index = first_seven_digits[-2]
                        if (self.password_index.count(index) > 0 ) and (self.used_indexes.count(index) == 0): 
                                password = first_seven_digits[-1]
                                self.password_two[int(index)] = password
                                self.used_indexes.append(index)
                                                        
                
                print self.password_two
                
if __name__ == "__main__":
        x = Chess()
#        x.doStuff()
        x.doStuffTwo()

