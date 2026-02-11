#!/usr/bin/env python3

import sys
import re

if len(sys.argv) <= 1:
	print("none")
else:
	phrase = sys.argv[1]
	keyword = "ism"

	scan = re.findall(keyword, phrase)

	if scan == keyword:
		print("")
	else:
		