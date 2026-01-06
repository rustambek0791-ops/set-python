import os
set1 = {"Artel","Alif","Yandex","Google","Meta"}
set2 = {"Google","Apple","Amazon","Meta"}
set3 = {"Alibaba","Uzum","Meta","Google","Amazon"}
set5 = set1.intersection(set2,set3)
set4 = set1.difference(set2,set3)
print(set5)
print(set4)