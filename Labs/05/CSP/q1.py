from ortools.sat.python import cp_model

distances = [10, 20, 15, 30]
product_frequencies = [5, 3, 2, 8]
num_products = len(distances)
slot_capacity = [3, 3, 3, 3]

model = cp_model.CpModel()

products = [model.new_int_var(0, len(distances) - 1, f"product_{i}") for i in range(num_products)]

# Constrain no. 1
for i in range(num_products):
    for j in range(i + 1, num_products):
        model.Add(products[i] != products[j])

# Constrain no. 2
for i in range(num_products):
    model.Add(products[i] < len(distances))

# Constrain no. 3
total_distance = sum(distances[products[i].Index()] * product_frequencies[i] for i in range(num_products))

model.Minimize(total_distance)

solver = cp_model.CpSolver()

status = solver.Solve(model)

print(f"Solver status: {solver.StatusName(status)}")

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Solver found a solution:")

    total_distance = 0

    for i in range(num_products):
        product_slot = solver.Value(products[i])
        print(f"Product {i} is assigned to slot {product_slot} with distance {distances[product_slot]} and frequency {product_frequencies[i]}")
        total_distance += distances[product_slot] * product_frequencies[i]

    print(f"Total walking distance: {total_distance}")
else:
    print("No solution found.")
