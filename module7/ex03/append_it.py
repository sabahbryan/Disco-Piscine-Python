#!/usr/bin/env python3

import sys
#import re

if len(sys.argv) <= 1:
	print("none")
else:
	phrase = sys.argv[1]
	#keyword = "ism"

	#scan = re.findall(keyword, phrase)
	scan = sys.argv[1].find("ism")

	if scan == True:
		print("")
	else:
		print(f"{sys.argv[1]}ism")


"""
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)
"""

# not skipping words with "ism"
# only reads 1st parameter (after program)