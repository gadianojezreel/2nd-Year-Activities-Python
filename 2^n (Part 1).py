#Determine the value of 2^n
print("2^n = ?")
n=eval(input("Enter power or the value of the exponent: "))
p=2**n

print("")
print("2 raised to the power of ", n, " is equal to ", p, ".", sep="")
print("Therefore, the last digit of 2^", n, sep="", end="")
print(" is ", (p%10), ".", sep="")
