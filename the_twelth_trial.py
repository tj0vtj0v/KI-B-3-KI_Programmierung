from unique import *

r1, r2, r3, r4, r5, r6, r7, r8, r9 = Ints("r1 r2 r3 r4 r5 r6 r7 r8 r9")
# -1 -> Tiger, 0 -> Empty, 1 -> Lady

s1 = Or([r1 == 1, r3 == 1, r5 == 1, r7 == 1, r9 == 1])
s2 = r2 == 0
s4 = Not(s1)
s5 = Xor(s2, s4)
s7 = Not(r1 == 1)
s3 = Xor(s5, Not(s7))
s6 = Not(s3)
s8 = And((r8 == -1), (r9 == 0))
s9 = And((r9 == -1), Not(s6))

rs = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
ss = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

c1 = And([And(-1 <= rs[i], rs[i] <= 1) for i in range(len(rs))])
c2 = Sum([rs[i] == 1 for i in range(len(rs))]) == 1
c3 = And([Implies(rs[i] == 1, ss[i]) for i in range(len(rs))])
c4 = And([Implies(rs[i] == -1, Not(ss[i])) for i in range(len(rs))])
c5 = r8 != 0

s = Solver()

s.add(c1)
s.add(c2)
s.add(c3)
s.add(c4)
s.add(c5)

s.check()

print(s.model())
unique(s, rs)
