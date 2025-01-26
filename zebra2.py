from unique import *

blue, green, orange, pink = Ints('blue green orange pink')
bol, chi, gre, pak = Ints('bold chi gre pak')
A, D, P, S = Ints('A D P S')
t8, t11, t26, t38 = Ints('t8 t11 t26 t38')

r1 = t26 == 3
r2 = t8 == 4
r3 = bol > orange
r4 = Abs(chi - D) == 1
r5 = t38 == 2
r6 = D == 4
r7 = orange == chi
r8 = Abs(t38 - P) == 1
r9 = pak == 2
r10 = blue == 2
r11 = pink - chi == 1
r12 = gre == S

shirts = [blue, green, orange, pink]
nats = [bol, chi, gre, pak]
exps = [A, D, P, S]
members = [t8, t11, t26, t38]

rules = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12]

c1 = And([
    And([
        And([1 <= l[i], l[i] <= 4]) for i in range(len(l))
    ]) for l in [shirts, nats, exps, members]
])

c2 = And([Distinct(l) for l in [shirts, nats, exps, members]])

s = Solver()

s.add(c1)
s.add(c2)
s.add(rules)

s.check()

print(s.model())
