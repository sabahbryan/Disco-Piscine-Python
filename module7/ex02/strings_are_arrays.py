#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 2:
	print("none")
else:
	phrase = sys.argv[1]
	keyword = "z"

	scan = re.findall(keyword, phrase)

	if len(scan) == 0:
		print("none")
	else:
		print(scan)

#output if 2 'z': ['z', 'z']
#need to modify