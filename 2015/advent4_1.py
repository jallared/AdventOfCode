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

first_five_digits = '11111'
while first_five_digits != '00000':
	answer += 1
	kod = md5.new()
	kod.update(my_input)
	kod.update(str(answer))
	first_five_digits = kod.hexdigest()
	first_five_digits = first_five_digits[0] + first_five_digits[1] + first_five_digits[2] + first_five_digits[3] +first_five_digits[4]

print answer
