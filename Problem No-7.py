# Write a python script to print first N even natural numbers in reverse order.
i=int(input("Enter the value of n to print first n even natural numbers in reverse order : "))
while(i>=1):
    print((2*i),end=" ")
    i=i-1
print()