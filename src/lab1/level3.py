def solution(numbers):
    max_length = 0
    last = len(numbers) - 1
    index = 1
    while index < last:
        if (numbers[index - 1] < numbers[index]) and (
            numbers[index] > numbers[index + 1]
        ):
            left = index - 1
            right = index + 1
            current_length = 3

            while left > 0 and numbers[left] > numbers[left - 1]:
                left -= 1
                current_length += 1

            while right < last and numbers[right] > numbers[right + 1]:
                right += 1
                current_length += 1

            max_length = max(current_length, max_length)

        index += 1

    return max_length
