'''Fibonacci Sequence - Enter a number and have the program
generate the Fibonacci sequence to that number or to the Nth number.'''
#I assume the "modern" Fib sequence starts with 0 ie first fib number = 0, 2nd = 1,etc.

__author__ = "Alin Dindareanu"

print("Input your number in the Fibonacci sequence: int n > 0: ")
n = int(input())

a = 0
b = 1
cp = n
while (cp > 2):
    a, b = b, a + b
    cp -= 1
print(b)

#solution using a recursive function
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(n))