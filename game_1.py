import sys
def check_points(points):
    if points>=50:
        print("YOU WON.........")
        sys.exit(1)
        

points=0
while(True):
    print("""****DICE**** 
          Dices have 0,1,2,3,4,5 to roll it""")
    dice=int(input("Role the dice : "))
    

    if dice==0:
        points=0
        print("YOU LOSS...........")
        sys.exit(1)
    elif dice%2==0:
        points+=2
        check_points(points)
        print("Your points now is",points)
    elif dice%2 !=0:
        if dice == 1 or dice ==3:
            print("you have to jump !!!!")
        elif dice==5:
            points+=3
            check_points(points)
            print("Your points now is",points)
                
