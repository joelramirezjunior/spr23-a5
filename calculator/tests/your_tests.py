#!/usr/bin/env python3
from calculator_adapter import run

# Subtraction test: checks that the program outputs "2" for an input of "5 - 3"
assert run("5 - 3").output == "2"

# Division test: checks that the program outputs "2" for an input of "10 / 5"
assert run("10 / 5").output == "2"

# Negation test: checks that the program outputs "-5" for an input of "0 - 5"
assert run("0 - 5").output == "-5"

# Large numbers test: checks that the program outputs "2000000" for an input of "1000000 + 1000000"
assert run("1000000 + 1000000").output == "2000000"

# Zero multiplication test: checks that the program outputs "0" for an input of "0 * 5"
assert run("0 * 5").output == "0"

# Non-integer division test: checks that the program outputs "2" for an input of "5 / 2"
assert run("5 / 2").output == "2"

print("All tests passed!")
