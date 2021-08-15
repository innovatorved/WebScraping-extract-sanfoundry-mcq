import re

marks = "1 2345"

# \d set to only one num characte
print("Matches: ",len(re.findall("\D", marks)))
print(re.findall("\D" , marks))


marks1 = "123 1234 12345 123456 1234567"

# se the size of number
# output is numbers , size greater than equal to 4 and less than 7
print("Matches1: ",re.findall("\d{4,7}", marks1)) 
