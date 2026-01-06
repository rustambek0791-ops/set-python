import os
set1={100, 20, 45, 80, 70, 50}
set2={30, 55, 70, 60, 20, 100}
set3= set1.intersection(set2)
for i in set3.copy():
    if i < 60:
        set3.discard(i)
summa=0
sanash=0
for i in set3:
    summa+=i
    sanash+=1
print(summa/sanash)
        
