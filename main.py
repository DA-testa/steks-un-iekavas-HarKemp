# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.insert(0,Bracket(next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0 or are_matching(opening_brackets_stack[0].char, next) != True:
                return i + 1
            opening_brackets_stack.pop(0)
            
    return "Success"

def main():
    text = input()
    if(text.find('I') != -1):
        mismatch = find_mismatch(text)
        if(mismatch == "Success"):
            print("Success")
        else:
            print(mismatch)


if __name__ == "__main__":
    main()
