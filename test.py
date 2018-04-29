import htmlgenpy as hgp
from random import randint

def randbool():
    if randint(0, 1) == 0:
        return False
    else:
        return True

print("=== STYLES ===")
print(hgp.Style.bold("bold"))
print(hgp.Style.italic("italic"))
print(hgp.Style.underline("underlined"))
print(hgp.Style.bools("random style", randbool(), randbool(), randbool()))
print("")

print("=== EMPTY HEADER ===")
test_header = hgp.Header.empty()
for line in test_header:
    print(line)
print("")


print("=== BASIC HEADER ===")
test_header = hgp.Header.basic("this is a title")
for line in test_header:
    print(line)
print("")

