#!/usr/bin/env python3

import sys

if len(sys.argv) <= 1:
	print("none")
else:
	print("Parameters:", len(sys.argv) - 1)

	for x in sys.argv[1:]:
		print(f"{x}" + ": " + f"{len(x)}")

# "[1:]" is slicing, to prevent printing of program name ~ 2nd element onwards
# [1:6] ~ from 2nd to 7th element, index starts at 0