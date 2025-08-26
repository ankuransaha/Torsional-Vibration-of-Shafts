import math
def three_rotor(Ia,Ib,Ic,l1,l2,ds,G):
  p=Ic/Ia
  a=(1+p)*Ic+Ib*p
  b=-((l1+p*l2)*Ib+Ic*(l1+l2))
  c=Ib*l1*l2
  lc1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
  lc2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
  la1=p*lc1
  la2=p*lc2
  J=(math.pi*ds**4)/32

  # Initialize variables to store the results
  freq_list=[0,0] ## Declared a null list to save frequencies

  if la1<l1 and lc1<l2:
    fns = (1/(2*math.pi))*math.sqrt(G*J/(Ia*la1))
    freq_list[0]=fns

  if la2<l1 and lc2<l2:
    fns = (1/(2*math.pi))*math.sqrt(G*J/(Ia*la2))
    freq_list[0]=fns

  if la1>l1 and lc1<l2:
    fnt = (1/(2*math.pi))*math.sqrt(G*J/(Ic*lc1))
    freq_list[1]=fnt

  if la2>l1 and lc2<l2:
    fnt = (1/(2*math.pi))*math.sqrt(G*J/(Ic*lc2))
    freq_list[1]=fnt

  if lc1>l2 and la1<l1:
    fnt = (1/(2*math.pi))*math.sqrt(G*J/(Ia*la1))
    freq_list[1]=fnt

  if lc2>l2 and la2<l1:
    fnt = (1/(2*math.pi))*math.sqrt(G*J/(Ia*la2))
    freq_list[1]=fnt

  # Return the frequencies stored in list
  return freq_list[0], freq_list[1]
