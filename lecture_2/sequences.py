name = "Alice"
coordinates = (10.0,20.0)
names = ["Alice", "Bob", "Charlie"]
print(name[0])
print(coordinates[0])
print(names[1])

for i in range(5):
    print(i)

for name in names:
    print(name)

s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(3)

print(s)

ages = {"Alice":22, "Bob":27}
ages["Charlie"] = 30
ages ["Alice"] +=1
print(ages)