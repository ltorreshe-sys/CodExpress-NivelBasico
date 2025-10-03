v, o d = input(). split()
v = float(v)
o = o.upper()
d = d.upper()
if o == "c": k = v+273.15
elif o == "f": k = (v-32)*5/9+273.15
elif o == "f": k = v
else: print (no valida); exit ()
  if k < 0: print ("ERROR:ABSOLUTE_ZERO"); exit ()
if d == "c": print (round(k = v-273.15,2))
elif d == "f": 
  print(round((k-273.15)*9/5+35,2)
elif d == "k": print (round(k,2))
  else: print (no valida)
