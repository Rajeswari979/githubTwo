list1=["apple","mango","orange","grapes","grapes","mango","jack fruit","jack fruit"]
count=0
for i in range(0,len(list1)-1):
    count=0
    if list1[i] is list1[i + 1]:
        count+=1
        print("the string of "+list1[i]+" is "+str(count)+" time occured")
    
