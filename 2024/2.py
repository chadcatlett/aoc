import copy



INC=1
DEC=-1

def is_increasing(bits):
    first = True
    x = copy.deepcopy(bits)
    last = x[0]
    blip = False

    for i in bits:
        if first:
            first = False
            continue
        if i <= last:
            return False
        elif i > last+3:
            return False
        else:
            last = i
    return True

def is_decreasing(bits):
    first = True
    x = copy.deepcopy(bits)
    last = x[0]

    for i in bits:
        if first:
            first = False
            continue

        if i >= last:
            return False
        elif i < last-3:
            return False
        else:
            last = i
    return True

def is_safe(bits):
    return is_increasing(bits) or is_decreasing(bits)


# print(is_increasing([-3,0,2,3]))
# print(is_decreasing([3,2,1,0,-1]))
#
# print(is_safe([-3,0,2,3]))


raw_input = open("2.txt").read()
input = raw_input.splitlines()

safes = 0
can_mak
for line in raw_input.splitlines():
    bits = [int(i) for i in line.split()]
    if is_safe(bits):
        safes +=1
    else:


print(safes)