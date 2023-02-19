# python3
# Keita Matvijuka 221RDB506 13. gr.

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    for i, char in enumerate(text):
        if char in "([{":
            # Push opening bracket onto stack
            stack.append((char, i))
        elif char in ")]}":
            if not stack:
                # If stack is empty, there's a closing bracket with no matching opening bracket
                return i
            else:
                top_char, top_pos = stack.pop()
                # Check for mismatching brackets
                if (top_char == "(" and char != ")") or \
                    (top_char == "[" and char != "]") or \
                    (top_char == "{" and char != "}"):
                    return i
    if stack:
        # If there are unmatched opening brackets, return their position
        return stack[0][1]
    else:
        # If all brackets match, return "Success"
        return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print(mismatch)
    else:
        print(mismatch + 1) # Add 1 to convert 0-indexed position to 1-indexed

if __name__ == "__main__":
    main()
