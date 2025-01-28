from unique import *

r1, r2, r3 = Bools('r1 r2 r3')

s1 = ~r2
s2 = ~r2
s3 = ~r1

c1 = Sum(r1, r2, r3) == 1
c2 = And(Implies(r1, s1), Implies(r2, s2), Implies(r3, s3))
c3 = Sum(s1, s2, s3) <= 2


s = Solver()

s.add(Or(s1, s2, s3))

s.add(c1)
s.add(c2)
s.add(c3)

s.check()

print(s.model())
unique(s, [r1, r2, r3])
