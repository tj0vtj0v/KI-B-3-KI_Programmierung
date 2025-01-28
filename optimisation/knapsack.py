from unique import *

cap = 20
vs = [1, 5, 12]
ws = [2, 4, 7]
vt = [Int(f"item{i}") for i in range(len(vs))]
value = Int("value")

c1 = Sum([
    vt[i] * ws[i] for i in range(len(vs))
]) <= cap

c2 = And([vt[i] >= 0 for i in range(len(vs))])

mc = value == Sum([
    vt[i] * vs[i] for i in range(len(vs))
])

o = Optimize()

o.add(c1)
o.add(c2)
o.add(mc)

o.maximize(value)

o.check()
print(o.model())