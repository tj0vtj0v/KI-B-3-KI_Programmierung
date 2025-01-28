from z3 import *

meeting_members = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 1]]
n = len(meeting_members)
meeting_slots = [Int(f"slot_meeting{i + 1}") for i in range(n)]

rule = And([
    Implies(
        meeting_slots[i] == meeting_slots[j],
        And([pers not in meeting_members[i] for pers in meeting_members[j]])
    )
    for i in range(n)
    for j in range(n)
    if i != j
])

c1 = And([
    And([meeting_slots[i] > 0, meeting_slots[i] <= 7]) for i in range(n)
])

slots = Int(f"slots")

def max_z3(values):
    if not values:
        return None  # Handle the empty case
    max_val = values[0]
    for v in values[1:]:
        max_val = If(v > max_val, v, max_val)
    return max_val

c2 = slots == max_z3([x for x in meeting_slots])

s = Optimize()

s.add(c1)
s.add(c2)
s.add(rule)

s.minimize(slots)

s.check()

print(s.model())
