from unique import *

black, green, orange, red, white = Ints("black green orange red white")
ivan, matthew, oscar, timothy, xavier = Ints("ivan matthew oscar timothy xavier")
court, lib, skyscraper, theatre, uni = Ints("court lib skyscraper theatre uni")
conan, laika, nipon, pantex, syno = Ints("conan laika nipon pantex syno")
dutch, german, greek, irish, peruvian = Ints("dutch german greek irish peruvian")
a25, a35, a40, a55, a60 = Ints("a25 a35 a40 a55 a60")

r1 = irish == a60
r2 = xavier - skyscraper == 1
r3 = peruvian == a55 # only spanish speakting?
r4 = Or(red == 1, red == 5)
r5 = white < irish
r6 = german == a25
r7 = green == uni
r8 = greek > white
r9 = timothy - lib == 1
r10 = black - xavier == 1
r11 = Abs(a55 - lib) == 1
r12 = green == a35
r13 = Abs(green - oscar) == 1
r14 = nipon == a60
r15 = Abs(lib - uni) == 1
r16 = syno == peruvian
r17 = black == theatre
r18 = white < a35
r19 = laika == a25
r20 = matthew - xavier == 1
r21 = xavier == conan
r22 = And([a40 < syno, syno < irish])


rules = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22]

bags = [black, green, orange, red, white]
names = [ivan, matthew, oscar, timothy, xavier]
buildings = [court, lib, skyscraper, theatre, uni]
cams = [conan, laika, nipon, pantex, syno]
nationalities = [dutch, german, greek, irish, peruvian]
ages = [a25, a35, a40, a55, a60]


c1 = And([
        And([
            And(1 <= l[i], l[i] <= 5) for i in range(len(l))
        ]) for l in [bags, names, buildings, cams, nationalities, ages]
])

c2 = And([Distinct(l) for l in [bags, names, buildings, cams, nationalities, ages]])

s = Solver()

s.add(And(rules))
s.add(c1)
s.add(c2)

s.check()

print(s.model())
