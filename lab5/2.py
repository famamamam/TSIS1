import re
txt=input()
x=re.search(r"ab{2,3}",txt)
print(x)