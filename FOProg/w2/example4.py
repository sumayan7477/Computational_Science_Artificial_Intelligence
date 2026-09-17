# Original
ss = "Drink your milk!"
print("Original string is: ", ss, "\n")

# Some slicing
print("ss[2:13]", "\t", ss[2:13]) # substring
print(r"ss[2:13:2]", "\t", ss[2:13:2]) # substring step 2

print("ss[::]", "\t\t", ss[::]) # The whole string
print("ss[::-1]", "\t", ss[::-1]) # The whole string - negative steps!

# Note also these
print("ss[-1:-5]", "\t", ss[-1:-5]) # by defaul steps are forward
print("ss[-1:-5:-1]", "\t", ss[-1:-5:-1]) # Here steps are backward
 
