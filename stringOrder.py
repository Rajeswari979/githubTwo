
str1="abcd"
str2="cdab"
check=[]
checks=[]
count=0
if len(str1) == len(str2):
    for i in range(0,len(str1)):
      check[i]=str1[i:i+1] 
check[-1]=str1[0:-1]   

for i in range(0,len(str1)):
        checks[i]=str2[i:i+1] 
checks[-1]=str1[0:-1]       


for i in range(len(str1)):
     print(check[i])


    
