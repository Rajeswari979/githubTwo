#Balancing the parenthesis
#example:(a),(a(b))
#false-)a(,(a))
#list=['(','a',')']

string=input("enter the string : ")
#str_list=list(string)
count=0

for i in string:
    if i=="(" :
        count+=1
    elif i==')' :
        count-=1

if count==0:
    print(f"{string} is ok ")

