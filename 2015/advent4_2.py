import string
import md5

my_input = 'bgvyzdsv'

test_input = 'abcdef'
test_answer = 609043
test_input_2 = 'pqrstuv'
test_answer_2 = 1048970

test_1 = md5.new()
test_1.update(test_input + str(test_answer))
print test_1.hexdigest()

test_2 = md5.new()
test_2.update(test_input_2 + str(test_answer_2))
print test_2.hexdigest()

answer = 0

first_six_digits = '111111'
while first_six_digits != '000000':
	answer += 1
	kod = md5.new()
	kod.update(my_input)
	kod.update(str(answer))
	first_six_digits = kod.hexdigest()
	first_six_digits = first_six_digits[0] + first_six_digits[1] + first_six_digits[2] + first_six_digits[3] +first_six_digits[4] + first_six_digits[5]

print answer
