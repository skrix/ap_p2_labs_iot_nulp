def people_relations(pairs):
    relations = {}
    people = set()

    for u, v in pairs:
        if u not in relations:
            relations[u] = []
        if v not in relations:
            relations[v] = []
        relations[u].append(v)
        relations[v].append(u)
        people.add(v)
        people.add(u)
    return people, relations

def compose_tribes(relations):
    visited = set()
    tribes = []

    for member in relations:
        if member in visited:
            continue

        stack = [member]
        visited.add(member)
        boys_count = 0
        girls_count = 0

        while stack:
            current = stack.pop()
            if is_girl(current):
                girls_count += 1
            else:
                boys_count += 1

            for neighbor in relations[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        tribes.append((boys_count, girls_count))
    return tribes


def is_girl(number):
    return bool(number % 2)

def solution(pairs:list[set]):
    people, relations = people_relations(pairs)

    if not people:
        return 0

    tribes = compose_tribes(relations)
    total_boys  = sum(boys for boys, _girls in tribes)
    total_girls = sum(girls for _boys, girls in tribes)

    total_possible_pairs = total_boys * total_girls
    internal_pairs = sum(boys * girls for boys, girls in tribes)

    return total_possible_pairs - internal_pairs
