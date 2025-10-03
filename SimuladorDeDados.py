N,s=map(input().split)
def g(seed):
  a=1664525;c=1013905223;m=2**32
  while true:
    seed=(a*seed+c)%m
    yield seed
gen=g(s)
f=[0]*6
for_in range (N);
f [next(gen)%6]+=1
for x in f; print(x)
