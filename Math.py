def abs(x):
	if x < 0:
		return -x
		
	return x
	
def sign(x):
	if x > 0:
		return 1
		
	if x < 0:
		return -1
		
	return 0

#numbers: set
def min(numbers):
	list_numbers = list(numbers)
	
	result = list_numbers.pop()
	while len(list_numbers) > 0:
		number = list_numbers.pop()
		if number < result:
			result = number
			
	return result
	
#numbers: set
def max(numbers):
	list_numbers = list(numbers)
	
	result = list_numbers.pop()
	while len(list_numbers) > 0:
		number = list_numbers.pop()
		if number > result:
			result = number
			
	return result
		
	
	