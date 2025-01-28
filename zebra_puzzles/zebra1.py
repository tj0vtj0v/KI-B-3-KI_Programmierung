from unique import *

black, orange, red, yellow = Ints("black orange red yellow")
Q, R, T, U = Ints("Q R T U")
oil, holder, chain, wallet = Ints("oil holder chain wallet")
accounting, IT, RD, sales = Ints("account IT RD sales")

r1 = chain == 2
r2 = T == 2
r3 = Or([yellow == 1, yellow == 4])
r4 = IT == 4
r5 = Or([oil == 1, oil == 4])
r6 = orange == 2
r7 = Abs(black - IT) == 1
r8 = orange < U
r9 = Abs(red - orange) == 1
r10 = chain == accounting
r11 = R == holder
r12 = wallet == IT
r13 = Abs(sales - U) == 1

rules = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13]

shirts = [black, orange, red, yellow]
names = [Q, R, T, U]
gifts = [oil, holder, chain, wallet]
deps = [accounting, IT, RD, sales]

c1 = And([
    And([
        And(1 <= l[i], l[i] <= 4) for i in range(len(l))
    ]) for l in [shirts, names, gifts, deps]
])

c2 = And([Distinct(l) for l in [shirts, names, gifts, deps]])

s = Solver()

s.add(And(rules))
s.add(c1)
s.add(c2)

s.check()

print(s.model())
