num=5
previous_number=""
for i in range(1,num+1):
    if i==1:
        previous_number=str(i)+previous_number
        print(previous_number)
    else:
        previous_number=str(i)+previous_number+str(i)
        print(previous_number)
