from ortools.sat.python import cp_model

distances = [1, 2, 3]
product_frequencies = [15, 8, 20]
product_volumes = [2, 1, 3]
slot_capacities = [3, 3, 3]

num_products = len(product_frequencies)
num_slots = len(distances)

model = cp_model.CpModel()

product_assignments = [model.NewIntVar(0, num_slots - 1, f"product_{i}") for i in range(num_products)]

model.AddAllDifferent(product_assignments)

cost_terms = []
for i in range(num_products):
    distance_var = model.NewIntVar(0, 100, f"distance_for_product_{i}")
    model.AddElement(product_assignments[i], distances, distance_var)

    cost = model.NewIntVar(0, 1000, f"cost_{i}")
    model.AddMultiplicationEquality(cost, [distance_var, product_frequencies[i]])
    
    cost_terms.append(cost)

model.Minimize(sum(cost_terms))

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Solution Found:\n")
    total = 0
    for i in range(num_products):
        slot = solver.Value(product_assignments[i])
        freq = product_frequencies[i]
        dist = distances[slot]
        print(f"Product {i} → Slot {slot} | Distance: {dist} | Frequency: {freq}")
        total += freq * dist
    print(f"\nTotal walking distance: {total}")
else:
    print("No solution found.")
