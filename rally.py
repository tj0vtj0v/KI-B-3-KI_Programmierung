from z3 import *

stopps = [Bool(f"s{i}") for i in range(1, 5)]
dists = [4, 8, 3, 7, 2]
fuels = [5, 10, 9, 8]

c1 = And([
    Sum(dists[:i]) <= Sum(
        [
            If(stopps[j], fuels[j], 0) for j in range(i)
        ] + [10]
    )
    for i in range(1, len(dists))
])

num_stopps = Int("num_stopps")

mc = num_stopps == Sum(stopps)

o = Optimize()

o.add(c1)
o.add(mc)
o.add(Or(stopps))

o.minimize(num_stopps)
o.check()

print(o.model())
