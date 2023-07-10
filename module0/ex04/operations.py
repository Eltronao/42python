import sys

def operations(a, b):
    try:
        A = int(a)
        B = int(b)
        print("Sum:         {}".format(A + B))
        print("Difference   {}".format(A - B))
        if B != 0:
            print("Quotient   {}".format(round(A / B, 4)))
            print("Remainder   {}".format(A % B))
        else:
            print("Error. Division by Zero.")
            print("Error. Module by Zero.")
    except ValueError:
	    print("AssertionError: argument is not an integer.")	

if __name__=="__main__":
	if len(sys.argv) < 3:
		print("Error. Too few arguments")
	elif len(sys.argv) != 3:
		print("Error. To many arguments.")
	else:	
		operations(sys.argv[1], sys.argv[2])