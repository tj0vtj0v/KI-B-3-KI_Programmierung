from unique import *

r1, r2 = Bools('r1 r2')

s1 = r1 | r2
s2 = ~r1

s = Solver()

s.add((s1 & s2) | (~s1 & ~s2))

s.check()

print(s)
print(s.model())
unique(s, [r1, r2])


