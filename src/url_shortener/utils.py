import random
import string

def code_generator(size=6, chars= string.ascii_letters + string.digits):
	# new_ele=''
	# for _ in range(size):
	# 	new_ele+=random.choice(chars)
	# return new_ele
	#The above is equivalent to the below command
	return ''.join(random.choice(chars) for _ in range(size))