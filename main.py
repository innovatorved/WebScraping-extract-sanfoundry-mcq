#!/usr/bin/env python3

from sanfoundryClass import copyit
import sys

# Enter the First Page Url of any topic you want
url = "https://www.sanfoundry.com/operating-system-questions-answers-basics/"


# print(len(sys.argv))
if len(sys.argv)==2:
	# print("yes")
	url = sys.argv[1]

data = copyit(url)
print(data.copyright())

# print(len(data.extract_list()))
# print(len(data.extract_dict()))
# print(data.extract_str()[:100])

data.extract_pdf()
