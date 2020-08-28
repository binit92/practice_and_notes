import argparse


# Getting Started 
# import argparse and give it a description  and set up a usage section
'''
parser = argparse.ArgumentParser(
description = " A simple argument parser", 
epilog = "This is where you might put example"  )

parser.print_help()
'''

# You won't be normally passing arguments from the command line after all
# so, we'll move this example inside a function inside a Python file.

def get_args():
	""""""
	parser = argparse.ArgumentParser(
	description = "A method argument parse",
	epilog = "This is where you might put an example"
	)
	return parser.parse_args()

#if __name__ == '__main__':
#	get_args()

# python 1CommandLineArguments.py -h

def get_args2():
	""""""
	parser = argparse.ArgumentParser(
	description = "A method argument parse",
	epilog = "This is where you might put an example"
	)

	# required argument 
	parser.add_argument('-x', 
	action='store',
	required=True, 
	help = "Help text for option X")

	#long option
	parser.add_argument('-w',
	'--execute',
	action='store',
	required=True,
	help='Help text for option w')

	#optional arguments
	parser.add_argument('-y',
	help = "Help text for option Y",
	default = "False")
	parser.add_argument('-z',
	help = "Help text for option Z",
	type = int)

	print(parser.parse_args())

#if __name__ == '__main__':
#	get_args2()


'''
What do you do if you have options that conflict with each other? 
A common example would be running your application in v
erbose mode versus quiet mode. You can run it in either mode, but not both. 
How do we prevent the user from running it that way though? 
It’s actually quite easy via the mutually_exclusive_group function
'''

def get_args3():
	""""""
	parser = argparse.ArgumentParser(
	description="A simple argument",
	epilog = "This is where you might put an example usage"
	)

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-x', '--execute', action="store", help='Help text for option X')
	group.add_argument('-y', help='Help text for option Y', default=False)

	parser.add_argument('-z', help='Help text for option Z', type=int)
	print(parser.parse_args())

if __name__ == '__main__':
	get_args3()