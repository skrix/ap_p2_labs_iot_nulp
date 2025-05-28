def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge_parts(left_half, right_half)


def merge_parts(left, right):
    sorted_merge_result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_merge_result.append(left[i])
            i += 1
        else:
            sorted_merge_result.append(right[j])
            j += 1

    sorted_merge_result.extend(left[i:])
    sorted_merge_result.extend(right[j:])

    return sorted_merge_result


def solution(nums):
    squared = [x * x for x in nums]
    return merge_sort(squared)
