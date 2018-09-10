import sys
total = 0
numbers = sys.stdin.read().split()

for x in numbers:
    total += float(x)
print(total/len(numbers))
