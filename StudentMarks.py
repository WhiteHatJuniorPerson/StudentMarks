import csv 
import numpy as np 

f = open("Student Marks vs Days Present.csv")
csvo = csv.reader(f)
data = list(csvo)
data.pop(0)
marks = []
dayspresent = []
for i in range(len(data)):
    m= float(data[i][1])
    d = float(data[i][2])
    marks.append(m)
    dayspresent.append(d)
d = {"x": dayspresent, "y": marks}
correlation  = np.corrcoef(d["x"],d["y"])
print(correlation)
