# two_rotor.py
import math
def two_rotor(L,Ia,Ib,ds,G):
  pi=math.pi
  J=(pi*ds**4)/32
  la=(Ib/(Ia+Ib))*L
  lb=(Ia/(Ia+Ib))*L
  fna=(1/(2*pi))*(G*J/(Ia*la))**0.5
  fnb=(1/(2*pi))*(G*J/(Ib*lb))**0.5
  return fna
"""[link text](https://) https://github.com/ankuransaha/Torsional-Vibration-of-Shafts.git"""
