def print_multiplication_table(n):
    x = 0
    while x<n:
        y = 0
        x = x + 1
        while y<n: 
            y = y + 1
            print str(x) + ' * ' + str(y) + ' = ' + str(x*y)

print_multiplication_table(10)