import sys
data = sys.argv[1]
print("Input: " + data)


# Recreating find() and rfind() for lists
def find_in_list(the_list, char, start_index=0):
    for index, token in enumerate(the_list[start_index:]):
        if token == char:
            return index + start_index
        
def rfind_in_list(the_list, char, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(the_list)
    for index, token in reversed(list(enumerate(the_list[start_index:end_index]))):
        if token == char:
            return index + start_index

def parse_element(e):
    if e == "True":
        return True
    elif e == "False":
        return False
    elif e[0] == "'" and e[-1] == "'":
        return e[1:-1]
    else:
        try:
            return int(e)
        except:
            pass
        try:
            return float(e)
        except:
            pass
        return e

data = data.replace(" ", "")  # Remove spaces from string to simplify

data_with_delimiters = data.replace("[", "[,").replace("]", ",]")
tokens = data_with_delimiters.split(",")  # Tokenizing data into numbers, '[', and ']'
tokens = [parse_element(token) for token in tokens]

tokens = tokens[1:-1]  # Remove initial brackets

while "[" in tokens:
    deepest_open_index = rfind_in_list(tokens, "[")
    deepest_close_index = find_in_list(tokens, "]", deepest_open_index)
    deepest_list = tokens[deepest_open_index + 1:deepest_close_index]

    # Delete the tokens of the list that was parsed
    tokens = tokens[:deepest_open_index] + tokens[deepest_close_index + 1:]

    # Replace the tokens with a list
    tokens.insert(deepest_open_index, deepest_list)

print(tokens)