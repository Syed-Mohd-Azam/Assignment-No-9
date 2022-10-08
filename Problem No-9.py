# Write a python script to print cubes of first N natural numbers.
i,n=1,int(input("Enter the value of n to print the cubes of first n natural numbers : "))
while(i<=n):
    print((i*i*i),end=" ")
    i=i+1
print()
