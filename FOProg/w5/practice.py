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
# %%
