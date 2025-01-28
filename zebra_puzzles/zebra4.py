from unique import *

black, green, pink, red, yellow = Ints('black green pink red yellow')
A, K, N, P, U = Ints('A K N P U')
caro, french, queen, ruy, sicilian = Ints('caro, french, queen, ruy, sicilian')
angolan, peruvian, filipino, hungarian, portuguese = Ints("angolan peruvian filipino hungarian portuguese")
adventure, fantasy, drama, scifi, horror = Ints("adventure, fantasy, drama, scifi, horror")
athen, geneva, moscow, munich, washington = Ints("athen, geneva, moscow, munich, washington")

shirts = [black, green, pink, red, yellow]
names = [A, K, N, P, U]
openings = [caro, french, queen, ruy, sicilian]
mentors = [angolan, peruvian, filipino, hungarian, portuguese]
books = [adventure, fantasy, drama, scifi, horror]
cities = [athen, geneva, moscow, munich, washington]

rules = [
    Abs(U - queen) == 1,
    Abs(portuguese - pink) == 1,
    geneva == scifi,
    And([horror < green, green < K]),
    And([munich < peruvian, peruvian < filipino]),
    Abs(adventure - moscow) == 1,
    red < filipino,
    moscow > yellow,
    portuguese - U == 1,
    Abs(drama - ruy) == 1,
    Abs(pink - ruy) == 1,
    Or([A == 1, A == 5]),
    washington - angolan == 1,
    green < angolan,
    Abs(munich - geneva) == 1,
    P == 2,
    Or([Abs(peruvian - black) == 1, Abs(portuguese - black) == 1, Abs(angolan - black) == 1]),
    And([geneva < french, french < adventure]),
    Abs(queen - drama) == 1,
    Or([athen == 1, athen == 5]),
    Abs(sicilian - yellow) == 1,
    Abs(K - fantasy) == 1
]

c1 = And([
    And([
        And([l[i] >= 1, l[i] <= 5]) for i in range(len(l))
    ]) for l in [shirts, names, openings, mentors, books, cities]
])

c2 = And([
    Distinct(l) for l in [shirts, names, openings, mentors, books, cities]
])

s = Solver()

s.add(c1)
s.add(c2)
s.add(rules)

s.check()

print(s.model())
unique(s, [v for l in [shirts, names, openings, mentors, books, cities] for v in l])
