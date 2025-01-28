from z3 import *

vs = [1, 3, 5]
ws = [1, 2, 3]
max_w = 8
n = len(vs)

ss = [Int(f"i{i}") for i in range(n)]

s_val = Sum([ss[i] * vs[i] for i in range(n)])
s_wgh = Sum([ss[i] * ws[i] for i in range(n)])

value = Int("value")

c1 = And([ss[i] >= 0 for i in range(n)])
c2 = s_wgh <= max_w

mc = value == s_val

s = Optimize()

s.add(c1)
s.add(c2)
s.add(mc)
s.maximize(value)

s.check()
print(s.model())
