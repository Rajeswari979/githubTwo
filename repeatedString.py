s = ["apple", "orange", "apple", "apple", "apple", "orange", "orange"]

count = 0
pre = s[0]
for i in range(1,len(s)-1):
    if pre == s[i]:
        count+=1
        pre = s[i]
        
print(count)        
    
