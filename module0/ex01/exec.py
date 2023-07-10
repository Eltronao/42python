import sys

def	main():
	n = len(sys.argv)
	if n > 1:
		print(" ".join(sys.argv[1:n:1]).swapcase()[::-1])

main()