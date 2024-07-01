from collections import defaultdict


def longest_substr_with_max_distinct_chars(text: str, max_distinct_chars: int) -> int:
    """
    Find the length of the longest substring that contains up to
    max_distinct_chars different characters.

    :param text: Input string.
    :param max_distinct_chars: Maximum number of distinct characters in the substring.
    :return: The length of the longest substring containing up to
    max_distinct_chars different characters.
    """
    if max_distinct_chars == 0:
        return 0

    left = 0
    max_length = 0
    char_count = defaultdict(int)

    for right in range(len(text)):
        char_count[text[right]] += 1
        while len(char_count) > max_distinct_chars:
            char_count[text[left]] -= 1
            if char_count[text[left]] == 0:
                del char_count[text[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
