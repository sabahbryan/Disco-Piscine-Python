#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("none")
else:
	pass1 = sys.argv[1]

	pass2 = input("What was the parameter? ")

	if len(sys.argv) != 2:
		print("none")
	else:
		#pass2 = sys.argv[1]
		if pass1 == pass2:
			print("Good job!")
		else:
			print("Nope, sorry...")