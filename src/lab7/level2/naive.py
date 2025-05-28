def solution(haystack: str, needle: str) -> tuple[int, int]:
    haystack_len = len(haystack) # string
    needle_len = len(needle) # substring
    comparisons = 0

    if needle_len == 0:
        return (None, 0)

    if needle_len > haystack_len:
        return (None, 0)

    last_match_start_index = None
    for i in range(haystack_len - needle_len + 1):
        is_match = True
        for j in range(needle_len):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                is_match = False
                break

        if is_match:
            last_match_start_index = i

    if last_match_start_index != None:
        return (last_match_start_index + needle_len, comparisons)
    else:
        return (None, comparisons)
