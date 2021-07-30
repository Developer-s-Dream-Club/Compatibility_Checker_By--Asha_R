name1 = input("Enter your name\n")
name2 = input("Ente your partner name\n")
combined = name1+name2
upper_name = combined.upper()
p = upper_name.count("L")
q = upper_name.count("O")
r = upper_name.count("V")
s = upper_name.count("E")
LOVE = p+q+r+s
if(LOVE < 1 or LOVE>9):
    print("Your love score is " , LOVE ,"you go together like coke and mentos")
elif(LOVE in range(4,6)):
    print("Your score is " , LOVE ,"you are alright together")
else:
    print("Your score is " , LOVE)
