from max_substr.core import longest_substr_with_max_distinct_chars


def test_longest_subst_with_max_distinct_chars_eng():
    assert longest_substr_with_max_distinct_chars("banana", 2) == 5
    assert longest_substr_with_max_distinct_chars("algorithm", 2) == 2


def test_longest_subst_with_max_distinct_chars_rus():
    assert longest_substr_with_max_distinct_chars("программирование", 2) == 3
    assert longest_substr_with_max_distinct_chars("мама", 2) == 4
