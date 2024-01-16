# Find the all factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
x = 52633
for i in range(1, x+1):
    if x % i == 0:
        print(i)
# Write a function that prints all factors of the given parameter x
def print_factor(x):
    # your code here
    for i in range(1, x+1):
        if x % i == 0:
            print(i)
# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
# your code here
for i in l:
    print('integer in the list:', i)
    print('its factors are:')
    for j in range(1, i+1):
        if i % j == 0:
            print(j)