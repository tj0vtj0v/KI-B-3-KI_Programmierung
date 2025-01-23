from unique import *

r1, r2, r3 = Bools('r1 r2 r3')

s1 = ~r1
s2 = r2
s3 = ~r2

c1 = Sum(r1, r2, r3) == 1
c2 = Sum(s1, s2, s3) == 1

s = Solver()

s.add(Or(s1, s2, s3))

s.add(c1)
s.add(c2)

s.check()

print(s.model())
unique(s, [r1, r2, r3])
