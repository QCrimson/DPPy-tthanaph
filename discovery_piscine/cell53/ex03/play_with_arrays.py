o = [2, 8, 9, 48, 8, 22, -12, 2]
print(o)
o = [x for x in o if x > 5]
n = [{y+2 for y in o}]
p = str(n).strip("[]")
print(p, end=" ")
