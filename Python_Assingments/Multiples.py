# Print all odd Numbers in range start from 1 to 1000
#
Numbers = range(1,1000)
for i in Numbers:
    if i%2!=0:
        print i

#Print All Multiple 5 Numbers
Numbers= range(5, 1000000)
for count in Numbers:
 if count%5==0:
     print count


#also this way!
Numbers = range(5, 1000, 5)
print Numbers*5
