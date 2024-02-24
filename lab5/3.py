import re
txt=input()
x=re.findall(r"[a-z_]+_[a-z]+",txt)
print(x)