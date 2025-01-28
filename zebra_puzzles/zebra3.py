from unique import *

black, green, pink, purple, white = Ints("black green pink purple white")
A, D, J, X, Y = Ints("A D J X Y")
brownie, cannoli, cake, mousse, pie = Ints("brownie cannoli cake mousse pie")
a25, a35, a45, a50, a55 = Ints("a25 a35 a45 a50 a55")
accountant, builder, receptionist, doctor, singer = Ints("accountant builder receptionist doctor singer")


r1 = doctor == 3
r2 = Or([receptionist == 1, receptionist == 5])
r3 = a50 - A == 1
r4 = pie == a50
r5 = a50 - a25 == 1
r6 = cannoli == builder
r7 = accountant == 1
r8 = Or([mousse == 1, mousse == 5])
r9 = Y == 1
r10 = X > white
r11 = white == 3
r12 = Or([a55 == 1, a55 == 5])
r13 = Abs(J - builder) == 1
r14 = And([a55 < black, black < a45])
r15 = a45 > black
r16 = Abs(a45 - X) == 1
r17 = a45 == builder
r18 = cake - cannoli == 1
r19 = D == purple
r20 = green == Y


shirts = [black, green, pink, purple, white]
names = [A, D, J, X, Y]
desserts = [brownie, cannoli, cake, mousse, pie]
ages = [a25, a35, a45, a50, a55]
profs = [accountant, builder, receptionist, doctor, singer]

rules = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

c1 = And([
    And([
        And([l[i] >= 1, l[i] <= 5]) for i in range(len(l))
    ]) for l in [shirts, names, desserts, ages, profs]
])

c2 = And([Distinct(l) for l in [shirts, names, desserts, ages, profs]])

s = Solver()

s.add(c1)
s.add(c2)
s.add(And(rules))

s.check()

print(s.model())
