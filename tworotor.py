## Frequency of Two Rotor
import numpy as np
def rotor_freq(L,Ia,Ib,ds,G):
  pi=math.pi
  J=(pi*ds**4)/32
  la=(Ib/(Ia+Ib))*L
  lb=(Ia/(Ia+Ib))*L
  fna=(1/(2*pi))*math.sqrt((G*J)/(Ia*la))
  fnb=(1/(2*pi))*(G*J/(Ib*lb))**0.5
  return fna
