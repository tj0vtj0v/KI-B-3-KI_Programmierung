from unique import *

r1, r2 = Bools('r1 r2')

s1 = ~r1 & ~r2
s2 = ~r2

c1 = r1 == s1
c2 = r2 != s2

s = Solver()

s.add(c1)
s.add(c2)

s.check()

print(s.model())
unique(s, [r1, r2])
