# MaxSubstringFinder

MaxSubstrFinder is a Python tool for finding substrings.

## Longest substring with max distinct chars
Finds the length of the longest substring that contains up to
max distinct chars.

```python
from max_substr import longest_substr_with_max_distinct_chars
text = "banana"
max_distinct_chars = 2
result = longest_substr_with_max_distinct_chars(text, max_distinct_chars)
print(result)  # Output: 5
# banana -> b[anana]
```