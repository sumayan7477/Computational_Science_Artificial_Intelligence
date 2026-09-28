num = float(input("enter a number :"))
print("num" , num)

def add_one(nr):
    x=nr+1
    return  x

num2 = add_one(num)
print("num2" , num2)


# %%

def Greeting(name , greeting = "Hello"):
    print(greeting + "," + name + "!" )

print(Greeting("sumaya" , "oi"))
print(Greeting("rubyat"))

# %% change a value of an array
a = [1,2,3,4,5]
print(a)
def change_val(list , value ,place):
    b= list
    b[int(place)]=value
    print(b)

change_val(a,7,4)
    
# %%
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count


# Example usage:
text = "Hello World"
result = count_vowels(text)
print(f"Number of vowels: {result}")  # Output: Number of vowels: 3
# %%
