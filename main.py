import optimization

def read_preferences(filename):
    preferences = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            student = parts[0]
            preferred = parts[1:]
            preferences[student] = preferred
    return preferences

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

def cost_function(solution, preferences):
    cost = 0
    for i, partner in enumerate(solution):
        student = str(i)
        if student in preferences:
            if partner == i:
                cost += 100  
            elif str(partner) in preferences[student]:
                cost += preferences[student].index(str(partner))
            else:
                cost += 10
    return cost

def print_solution(solution, preferences):
    print("Project Partnerships:")
    for i, partner in enumerate(solution):
        print(f"Student {i} is paired with Student {partner}")

def main():
    preferences = read_preferences('preferences.txt')
    method_choice = select_optimization_method()
    domain = create_domain(preferences)
    cost_func = lambda sol: cost_function(sol, preferences)
    solution = apply_optimization(method_choice, domain, cost_func)
    print_solution(solution, preferences)

if __name__ == "__main__":
    main()
