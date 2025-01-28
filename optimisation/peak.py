from unique import *

points = [3, 5, 4, 6, 8, 5, 2, 4, 1]

l, p, r = Ints("l p r")
length = Int("length")

c1 = And([l >= 0, l <= p, p <= r, r < len(points)])
c2 = And([Implies(And([l <= i, i < p]), points[i] < points[i+1]) for i in range(len(points)-1)])
c3 = And([Implies(And([p <= i, i < r]), points[i] > points[i+1]) for i in range(len(points)-1)])

mc = length == Sum([And([l <= i, i <= r]) for i in range(len(points))])

o = Optimize()

o.add(c1)
o.add(c2)
o.add(c3)
o.add(mc)

o.maximize(length)

o.check()
print(o.model())

