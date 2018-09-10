while True:
    n = int(input("Please enter n for factorial: "))
    if n < 0:
        print("Sorry number must be greater than 0.") 
        continue
    break

def factorial(val):
    if val < 0:
        return -1
    if val == 1:
        return 1
    return val * factorial(val-1)

print(factorial(n))
