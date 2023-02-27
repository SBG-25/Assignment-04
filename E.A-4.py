########## Problem-1
num=int(input('Enter the Number==>'))
fun = lambda b : b + 25
print(fun(num))

############ Problem-2
def triplenumber(numbers):
    result = {}
    for n in numbers:
        result[n] = n+n+n
    return result
numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
y=list(triplenumber(numbers).values())
print("The suqare of each is", y)

########### Problem-3

def squareEach(numbers):
    result = {}
    for n in numbers:
        result[n] = n ** 2
    return result
numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
y=list(squareEach(numbers).values())
print("The suqare of each is", y)






