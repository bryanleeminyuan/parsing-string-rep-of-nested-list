import sys
data = sys.argv[1]
print("Input: " + data)


# A [ increases the level of nested lists, and a ] decreases it.
# When the level reaches 0, the given list has ended.
def find_closing_index(stream):
    level = 0
    for index, char in enumerate(stream):
        if char == "[":
            level += 1
        if char == "]":
            level -= 1
            if level == 0:
                return index

# Try to parse the string into different formats
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

data = data.replace(" ", "")
def get_list(stream):
    e = ""  # The current element
    return_list = []

    index = 0
    while index < len(stream):
        char = stream[index]
        if char == "[":
            if index != 0:
                # If a opening bracket is found after the initial one,
                # recurse the substream and append it to the return list.
                substream = stream[index:find_closing_index(stream[index:]) + index + 1]
                return_list.append(get_list(substream))
                # Skip the parsed characters
                index += len(substream)
                continue
        # If a comma is found, parse the element cache and append it to the
        # cache list and reset the element cache.
        elif char == ",":
            if e != "":
                return_list.append(parse_element(e))
            e = ""
        # If an end bracket is found, parse the element cache and append it
        # to the cache list and return the final list.
        elif char == "]":
            if e != "":
                return_list.append(parse_element(e))
            return return_list
        # If no special characters are found, add the character to the
        # element cache.
        else:
            e += char
        index += 1

print(get_list(data))
