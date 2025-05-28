def partition(numbers, selected_number):
    left, middle, right = [], [], []

    for number in numbers:
        if number > selected_number:
            left.append(number)  # Larger numbers
        elif number < selected_number:
            right.append(number)  # Smaller numbers
        else:
            middle.append(number)  # Equal to number (duplications)

    return left, middle, right


def quickselect(numbers, k):
    selected_number = numbers[k - 1]
    left, middle, right = partition(numbers, selected_number)

    if k <= len(left):
        return quickselect(left, k)  # Search left
    elif k <= len(left) + len(middle):
        return selected_number  # Found
    else:
        return quickselect(right, k - len(left) - len(middle))  # Search right


def solution(numbers, k):
    if len(numbers) < k:
        return None, None

    element = quickselect(numbers, k)
    position = numbers.index(element)

    return element, position
