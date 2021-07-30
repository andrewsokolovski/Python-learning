a = int(input("Enter number whose factorial is required "))  # ask user to enter number
d = int(input("Enter number whose factorial is required "))  # ask user to enter number
n = int(input("Enter number whose factorial is required "))
sum = 0
i = 1
while i <= n:
    term = a + (i-1)*d
    print('The ' + str(i) + 'th term is ' + str(term))
    sum = sum + term
    i = i + 1
else:
    print('The sum of ' + str(n) + ' terms is\t:' + str(sum))
