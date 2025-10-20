def get_sorted(lst):
	result = list(lst)
	
	size = len(lst)
	for index in range(size):
		for j in range(size - index - 1):
			k = j + 1
			
			if result[j] >= result[k]:
				continue
				
			temp = result[k]
			result[k] = result[j]
			result[j] = temp

	return result
	
def get_sliced(list, start, end):
	result = []
	for index in range(start, end, 1):
		result.append(list[index])
		
	return result
	
def divide(list, number):
	result = []
	
def get_reversed(lst):
	result = list()
	for i in range(len(lst) - 1, -1, -1):
		result.append(lst[i])
	
	return result
	