# tworotor.py
import numpy as np
def tworotor(L,Ia,Ib,ds,G):
  pi=math.pi
  J=(pi*ds**4)/32
  la=(Ib/(Ia+Ib))*L
  lb=(Ia/(Ia+Ib))*L
  fna=(1/(2*pi))*math.sqrt((G*J)/(Ia*la))
  fnb=(1/(2*pi))*(G*J/(Ib*lb))**0.5
  return fna
def eq_rotor(l1,l2,l3,l4,d1,d2,d3,d4)
  return(0)

"""[link text](https://) https://github.com/ankuransaha/Torsional-Vibration-of-Shafts.git"""
