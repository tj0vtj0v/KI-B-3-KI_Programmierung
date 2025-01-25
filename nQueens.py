from unique import *

field = [Int(f"col{l}") for l in range(1, 9)]

c1 = And([And([1 <= field[i], field[i] <= 9]) for i in range(len(field))])
c2 = Distinct(field)
c3 = And([Abs(field[c1] - field[c2]) != Abs(c1 - c2) for c1 in range(8) for c2 in range(8) if c1 != c2])

s = Solver()

s.add(c1)
s.add(c2)
s.add(c3)

s.check()

print(s.model())
