#equivalent_shaft.py
def eqshaft_length(eqd,n):
import math
L_eq=0
shaft_dia=n*[0]
shaft_length=n*[0]
for i in range(n):
  shaft_dia[i]=float(input(f"Enter shaft diameter {i+1} :\t"))
  shaft_length[i]=float(input(f"Enter shaft length {i+1}:\t\t"))

for i in range(n):
  L_eq=L_eq+shaft_length[i]*(d/shaft_dia[i])**4

print(f"Equivalent length of the shaft is : {L_eq:0.3f}")
