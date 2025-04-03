def solution(cows, sections):
    sections = sorted(sections)
    low = sections[0] - sections[1]
    high = sections[-1] - sections[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2

        if is_possible(sections, cows, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

        return result


def is_possible(sections, cows, distance):
    placed_cows = 1
    current = sections[0]

    for section in sections:
        if section - current >= distance:
            placed_cows += 1
            current = section
        if placed_cows >= cows:
            return True
    return False
