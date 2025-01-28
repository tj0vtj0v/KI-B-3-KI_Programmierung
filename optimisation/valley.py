from unique import *

xs = [1, 8, 5, 3, 6, 4, 9, 4, 6, 8, 9]

f = Function("f", IntSort(), IntSort())
f_is_xs = And([f(i) == xs[i] for i in range(len(xs))])

l, r = Ints("l r")
length = Int("length")

c1 = And([l >= 0, l <= r, r < len(xs)])
c2 = And([
    Implies(
        And([l<i, i<r]),
        And([f(l) >= f(i), f(r) >= f(i)])
    ) for i in range(len(xs))
])

mc = length == r-l

o = Optimize()

o.add(f_is_xs)
o.add(c1)
o.add(c2)
o.add(mc)

o.maximize(length)

o.check()

print(o.model())
