# module_attribute.py - you can add an attribute to any module name.

import poll

poll.random_attribute = 1

print(f"poll.random_attribute = {poll.random_attribute}")

del poll.random_attribute

try:
    print(f"poll.random_attribute = {poll.random_attribute}")
except AttributeError:
    print(f"The poll.random_attribute was deleted.")
