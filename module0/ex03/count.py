import sys

def text_analyzer(*argv):
	'''\nThis function counts the number of upper characters, lower characters,punctuation and spaces in a given text.\n'''
	argc = 0
	for s in argv:
		argc += 1
	if (argv == 0):
		print("Error No text to analyze.")
	if (argc >= 2):
		print("Error. More than one string provided.")
	else:
		c = len(s)
		up = 0
		lo = 0
		pm = 0
		sp = 0
		for i in s:
			if (i in '¡!¿?,.:;()' or i == 39 or i == 34):
				pm += 1
			elif (i.isupper()):
				up += 1
			elif (i.islower()):
				lo += 1
			elif (i.isspace()):
				sp += 1
		print("The text contains {} character(s)".format(c))
		print("- {} upper letters".format(up))
		print("- {} lower letters".format(lo))
		print("- {} punctuation mark(s)".format(pm))
		print("- {} space(s)".format(sp))
	
if __name__=="__main__":
	if len(sys.argv) < 2:
		print("No text input to analyze.")
	elif len(sys.argv) != 2:
		print("Error. To many arguments.")
	else:	
		text_analyzer(sys.argv[1])
