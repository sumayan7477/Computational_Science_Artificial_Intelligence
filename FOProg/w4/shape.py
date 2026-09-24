n = int (input("Enter the number of rows for the rhombus: "))

while n%2==0:
    n = int (input("Enter the number of rows for the rhombus: "))

for i in range(1,n+1):
    if i<= (n+1)//2:
        stars = i
    else:
        stars = (n - i) + 1
    spaces =  (n + 1)//2 - stars
    print(" " * spaces + "* "* stars +"  "*spaces + "* "*stars  +"  "*spaces + "* "*stars  )