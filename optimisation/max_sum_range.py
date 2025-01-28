from unique import *

o = Optimize()

xs = [-2, 4, -5, 7, -8, 5, 2, 5, -6, 8, -2, 1]
l, r = Ints("l, r")

ss = Sum([If(And([l <= i, r >= i]), xs[i], 0) for i in range(len(xs))])

c1 = And([l>= 0, r < len(xs), l < r])

o.add(c1)

o.maximize(ss)

o.check()
print(o.model())
