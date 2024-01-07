import optimization

def read_preferences(filename):
    preferences = {}
    names = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(':')
            student = parts[0].strip()
            names.append(student)
            preferred = [p.strip() for p in parts[1].split(',')] if len(parts) > 1 else []
            preferences[student] = preferred
    return preferences, names


def select_optimization_method():
    print("Select Optimization Method: 1. Random, 2. Hill Climbing, 3. Simulated Annealing, 4. Genetic Algorithm")
    choice = int(input("Enter choice (1-4): "))
    return choice

def apply_optimization(method, domain, cost_func):
    if method == 1:
        return optimization.randomoptimize(domain, cost_func)
    elif method == 2:
        return optimization.hillclimb(domain, cost_func)
    elif method == 3:
        return optimization.annealingoptimize(domain, cost_func)
    elif method == 4:
        return optimization.geneticoptimize(domain, cost_func)

def create_domain(preferences):
    return [(0, len(preferences) - 1) for _ in preferences]

def cost_function(solution, preferences, names):
    cost = 0
    for i, partner_idx in enumerate(solution):
        if i == partner_idx:  # Penalize self-pairing
            cost += 100
        else:
            student = names[i]
            partner = names[partner_idx]
            if partner in preferences[student]:
                cost += preferences[student].index(partner)
            else:
                cost += 10  # Penalize if partner not in preferred list
    return cost

def print_solution(solution, names, preferences):
    print("Project Partnerships:")
    for i, partner_idx in enumerate(solution):
        if i != partner_idx:  # Skip self-pairing in output
            print(f"{names[i]} is paired with {names[partner_idx]}")
    # Calculate total cost within this function scope
    total_cost = cost_function(solution, preferences, names)
    print(f"Total Cost: {total_cost}")

def main():
    preferences, names = read_preferences('preferences.txt')
    method_choice = select_optimization_method()
    domain = create_domain(preferences)
    cost_func = lambda sol: cost_function(sol, preferences, names)
    solution = apply_optimization(method_choice, domain, cost_func)
    print_solution(solution, names, preferences)  # Now passing preferences

if __name__ == "__main__":
    main()