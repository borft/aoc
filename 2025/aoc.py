import os, sys


def input(test: bool = False) -> list:

	if test:
		filename = 'test.txt'
	else:
		filename = 'input.txt'
	filename = os.path.dirname(os.path.realpath(sys.argv[0])) + '/' + filename


	ret = []
	with open(filename, 'r') as file:
		for line in file:
			ret.append(line.strip())
	return ret
