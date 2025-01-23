from unique import *

r1, r2, r3 = Ints('r1 r2 r3')
# -1 -> T, 0 -> E, 1 -> L

s1 = r3 == 0
s2 = r1 == -1
s3 = r3 == 0

c1 = And(And(-1 <= r1, r1 <= 1), And(-1 <= r2, r2 <= 1), And(-1 <= r3, r3 <= 1))
c2 = Sum(r1, r2, r3) == 0
c3 = r1 != r2
c4 = And(Implies(r1 == 1, s1), Implies(r2 == 1, s2), Implies(r3 == 1, s3))
c5 = And(Implies(r1 == -1, ~s1), Implies(r2 == -1, ~s2), Implies(r3 == -1, ~s3))

s = Solver()

s.add(Or(s1, s2, s3))

s.add(c1)
s.add(c2)
s.add(c3)
s.add(c4)
s.add(c5)

s.check()

print(s.model())
unique(s, [r1, r2, r3])
