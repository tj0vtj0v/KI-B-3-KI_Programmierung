from z3 import *


def unique(solver, vars):
    m = solver.model()
    for v in vars:
        solver.push()
        solver.add(v != m.eval(v))
        if solver.check() == sat:
            print("other model:", solver.model())
        solver.pop()
    print("no other models")
