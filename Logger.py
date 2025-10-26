def new(name):
	def print(object, prefix = "PRINT"):
		time = str(get_time())
		quick_print(time + "-" + name + "-" + prefix + ": " + str(object))
	
	def debug(object):
		print(object, "DEBUG")
	
	def info(object):
		print(object, "INFO")
		
	def warning(object):
		print(object, "WARNING")
		
	def error(object):
		print(object, "ERROR")
		
	def critical(object):
		print(object, "CRITICAL")
	
	return {
		"debug": debug,
		"info": info,
		"warning": warning,
		"error": error,
		"criticalk": critical
	}
	