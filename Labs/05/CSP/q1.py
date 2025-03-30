from ortools.sat.python import cp_model

model = cp_model.CpModel()
p1, p2, p3 = [model.new_int_var(0, 2, f"p{i}") for i in range(1, 4)]

model.add_all_different([p1, p2, p3])

solver = cp_model.CpSolver()
if solver.solve(model) in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print(f"Product 1 -> Slot {solver.value(p1)}")
    print(f"Product 2 -> Slot {solver.value(p2)}")
    print(f"Product 3 -> Slot {solver.value(p3)}")
else:
    print("No solution found")
