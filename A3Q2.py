import sys


def project_selection(c):
    current_states = {0: c}

    for group in cr:
        next_states = {}
        for cost, revenue in group:
            for last_cost, capital in current_states.items():
                if cost > last_cost and cost <= capital:
                    capital_n = capital + revenue - cost
                    if cost not in next_states or capital_n > next_states[cost]:
                        next_states[cost] = capital_n

        if not next_states:
            return "impossible"

        max_capital = -1
        restate = {}
        for cost in sorted(next_states):
            capital = next_states[cost]
            if capital > max_capital:
                max_capital = capital
                restate[cost] = capital

        current_states = restate

    if current_states:
        return max(current_states.values())
    else:
        return "impossible"

# Read input data
a = [int(s) for s in sys.stdin.readline().split()]
cr = []
for _ in range(a[0]):
    line = sys.stdin.readline().strip()
    projects = []
    if line:
        for s in line.split():
            c, r = s.split(':')
            projects.append((int(c), int(r)))
    projects.sort()
    cr.append(projects)

init_cap = []
while len(init_cap) < a[1]:
    line = sys.stdin.readline()
    if not line:
        break
    init_cap.extend([int(s) for s in line.strip().split()])

for i in range(a[1]):
    result = project_selection(init_cap[i])
    print(result)
