def everyoneLikes(mine,frd1,frd2,frd3):
    eolikes = []
    for movie in mine:
        if movie in frd1 and movie in frd2 and movie in frd3:
            eolikes.append(movie)
    return eolikes

def nooneLikes(mine,frd1,frd2,frd3):
    nolikes = []
    for movie1 in mine:        
        if movie1 not in frd1 and movie1 not in frd2 and movie1 not in frd3:
            nolikes.append(movie1)
    return nolikes

def allNotmine(mine,frd1,frd2,frd3):
    alikes = []
    friendsLike = []
    for movie2 in frd1:
        if movie2 in frd3 and movie2 in frd2:
            friendsLike.append(movie2)
    for movie3 in friendsLike:
        if movie3 not in mine:
            alikes.append(movie3)
    return alikes

def checks(friend,notPeferable):
    morethan_onelike = []
    morethan = []
    # print(friend,notPeferable)
    for j in friend:
        if j in notPeferable:
            morethan_onelike.append(j)
            morethan.append(friend)
    return morethan,morethan_onelike

def likeTwo(eolikes,nolikes,mine,frd1,frd2,frd3):
    notPeferable = []
    mn = eolikes + nolikes
    for h in mine:
        if h not in mn:
            notPeferable.append(h)
    friends=[frd1,frd2,frd3]
    for friend in friends:
        result3=checks(friend,notPeferable)
            
    return result3
    

mine = ["a","b","c","d","e"]
frd1 = ["c","a","h","z","j"]
frd2 = ["d","g","z","a","c"]
frd3 = ["q","z","a","t","c"]
everyoneLike = []
firstTwo = []

result1 =everyoneLikes(mine,frd1,frd2,frd3)
result2 =nooneLikes(mine,frd1,frd2,frd3)
print(f"Everyone likes everyLikes",result1)
print( f"No one likes the movie except mine is ",result2)

print(f"Everyone likes except mine is ",allNotmine(mine,frd1,frd2,frd3))
print(f"Everyone likes except two is ",likeTwo(result1,result2,mine,frd1,frd2,frd3))

