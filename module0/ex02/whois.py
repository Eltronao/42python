import sys

def main():
	n = len(sys.argv)
	if (n == 2):
		try:
			x = int (sys.argv[1])
			if (x == 0):
				print("I'm Zero.")
			elif (x % 2 == 0):
				print("I'm even.")
			else:
				print("I'm odd.")
		except ValueError:
			print("AssertionError: argument is not an integer.")	
				
main()