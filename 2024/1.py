left = []
right = []

raw_input = open("1.txt").read()
input = raw_input.splitlines()
for i in input:
    bits = i.split(' ', 1)
    left.append(int(bits[0].strip()))
    right.append(int(bits[1].strip()))

left.sort()
right.sort()

distances = []

for i in zip(left, right):
    distances.append(abs(i[0] - i[1]))

print(sum(distances))

freq = []

for i in left:
        freq.append(i*right.count(i))
print(sum(freq))