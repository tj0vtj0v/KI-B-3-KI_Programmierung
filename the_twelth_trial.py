from unique import *

rs = [Int(f"r{n}") for n in range(9)]
# -1 -> Tiger, 0 -> Empty, 1 -> Lady

s0 = Or([rs[i] == 1 for i in range(9) if i % 2 == 0])
s1 = rs[1] == 0
s3 = ~s0
s4 = (s1 & ~s3) | (~s1 & s3)
s6 = rs[0] != 1
s2 = (s4 & s6) | (~s4 & ~s6)
s5 = ~s2
s7 = (rs[7] == -1) & (rs[8] == 0)
s8 = (rs[8] == -1) & ~s5

ss = [s0, s1, s2, s3, s4, s5, s6, s7, s8]

c1 = And([And(-1 <= rs[i], rs[i] <= 1) for i in range(9)])
c2 = Sum([If(rs[i] == 1, 1, 0) for i in range(9)]) == 1
c3 = And([Implies(rs[i] == 1, ss[i]) for i in range(9)])
c4 = And([Implies(rs[i] == -1, ~ss[i]) for i in range(9)])
c5 = rs[7] != 0

s = Solver()

s.add(Or(ss + [True]))  # + [True] even tho lady s_ has to be true

s.add(c1)
s.add(c2)
s.add(c3)
s.add(c4)
s.add(c5)

s.check()

print(s.model())
unique(s, rs)
