# How to use

Simply call the script followed by a string representation of a list to get the result.

`string_to_list_recursion.py` uses a recursive method to build a list from the outer-most layer inwards.

`string_to_list_replacement.py` tokenises the string into a list of `'['`, `']'`, and elements before continually replacing tokens with the list they represent, working from the inner-most layer outwards until no more nested lists can be converted.

## Example
`$ python string_to_list_replacement.py "[1, [2, 3]]"`

`> Input: [1, [2, 3]]`

`> [1, [2, 3]]`
