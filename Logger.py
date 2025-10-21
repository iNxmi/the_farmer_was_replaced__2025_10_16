def new(name):
	def print(string, prefix = "PRINT"):
		time = str(get_time())
		quick_print(time + "-" + name + "-" + prefix + ": " + string)
	
	def debug(string):
		print(string, "DEBUG")
	
	def info(string):
		print(string, "INFO")
		
	def warning(string):
		print(string, "WARNING")
		
	def error(string):
		print(string, "ERROR")
		
	def critical(string):
		print(string, "CRITICAL")
	
	return {
		"debug": debug,
		"info": info,
		"warning": warning,
		"error": error,
		"critical": critical
	}
	