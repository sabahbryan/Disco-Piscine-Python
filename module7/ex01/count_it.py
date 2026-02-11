#!/usr/bin/env python3

import sys

if len(sys.argv) <= 1:
	print("none")
else:
	print("Parameters:", len(sys.argv) - 1)

	for x in sys.argv:
		#print(x, len(x))
		print(f"{x}" + ": " + f"{len(x)}")

#need to stop printing program name