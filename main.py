# python3
# Keita Matvijuka 221RDB506 13. gr.

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    for i, char in enumerate(text):
        if char in "([{"
            stack.append((char, i))
        elif char in ")]}":
            if not stack:
  
                return i
            else:
                top_char, top_pos = stack.pop()
                # Check for mismatching brackets
                if (top_char == "(" and char != ")") or \
                    (top_char == "[" and char != "]") or \
                    (top_char == "{" and char != "}"):
                    return i
    if stack:

        return stack[0][1]
    else:

        return "Success"

def main():
    text = input()
if "I" in text:
    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print(mismatch)
    else:
        print(mismatch + 1)

if __name__ == "__main__":
    main()
