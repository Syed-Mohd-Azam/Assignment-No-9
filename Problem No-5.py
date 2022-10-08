# Write a python script to print first N odd natural numbers in reverse order.
i=((int(input("Enter the value of n to print first n natural numbers in reverse order: ")))-1)
while(i>=0):
    print((2*i+1),end=" ")
    i=i-1
print()