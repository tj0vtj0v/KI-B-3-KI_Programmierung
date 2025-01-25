from random import randint

import matplotlib
import matplotlib.pyplot as plt

from unique import *


def nullsum(num: int, bound: int):
    t = [randint(-bound, bound) for _ in range(num)]

    ts = [Bool(f"t{i}") for i in range(len(t))]

    p1 = Sum([If(ts[i], t[i], 0) for i in range(len(t))]) == 0
    p2 = Or(ts)

    le = Int("le")
    m1 = Sum(ts) == le

    o = Optimize()

    o.add(p1)
    o.add(p2)
    o.add(m1)

    o.maximize(le)

    if str(o.check()) == 'sat':
        return 1
    else:
        return 0


res = {}
reps = 100
bounds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 70, 100, 150, 200, 300, 400, 500, 700, 1000]

for bound in bounds:
    res[bound] = {}
    for l in range(1, 25):
        print(f"l={l}, bound={bound}")
        res[bound][l] = 0
        for _ in range(1, reps + 1):
            res[bound][l] += nullsum(l, bound)
        res[bound][l] /= reps

matplotlib.use('TkAgg')
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cmap = plt.get_cmap('copper')
norm = plt.Normalize(min(bounds), max(bounds))

for bound in bounds:
    x = list(res[bound].keys())
    y = [bound] * len(x)
    z = list(res[bound].values())
    ax.plot(x, y, z, marker='o', color=cmap(norm(bound)), label=f'Bound {bound}')

ax.set_xlabel('List length')
ax.set_ylabel('Bound')
ax.set_zlabel('Solvable ratio')
ax.set_title('Null sums in Lists with varying bounds')

ax.view_init(azim=92, elev=1)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, label='Bound')

plt.show(block=True)
