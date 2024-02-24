import re
txt=input()
x = re.search(r"\w+", txt)
print(x)