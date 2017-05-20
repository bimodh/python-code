#Argsort a list
#Return index of a sorted list

myList = [10,30,40,20,50]

print "input list : "+str(myList)

srt = sorted(myList)

print "sorted list : "+str(srt)

outArr = []
for i in range(0, len(srt)):
    outArr.append( myList.index(srt[i]))
    
print outArr
