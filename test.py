from z3 import *

x1 = Bool('x1')
x2 = Bool('x2')
x3, x4 = Bools('x3 x4')

t1 = Or(Or([x1, Not(x2), And(x3, Not(x4))]))
t2 = Or(Not(x1), x4)
t3 = Or(x2, Not(x4))

cond = And(t1, t2, t3)

s = Solver()

s.add(cond)  # add([t1, t2, t3])

print(s.check())

m = s.model()
print(m)

s.add(x3 != m[x3])

print(s.check())

print(s.model())

print(solve(cond))
