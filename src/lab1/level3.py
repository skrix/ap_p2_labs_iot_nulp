def solution(numbers):
    max_sequence_length = 0
    last_index = len(numbers) - 1
    index = 1
    while index < last_index:
        if (numbers[index - 1] < numbers[index]) and (
            numbers[index] > numbers[index + 1]
        ):
            left_index = index - 1
            right_index = index + 1
            current_sequence_length = 3

            while left_index > 0 and numbers[left_index] > numbers[left_index - 1]:
                left_index -= 1
                current_sequence_length += 1

            while (
                right_index < last_index
                and numbers[right_index] > numbers[right_index + 1]
            ):
                right_index += 1
                current_sequence_length += 1

            max_sequence_length = max(current_sequence_length, max_sequence_length)

        index += 1

    return max_sequence_length
