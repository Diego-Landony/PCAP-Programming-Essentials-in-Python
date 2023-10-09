#!/usr/bin/python3
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")


"""
As you can see, the empty print() invocation is not as empty as you may have expected ‒ it does output an empty line, or (this interpretation is also correct) it outputs a newline.
This is not the only way to produce a newline in the output console. We're now going to show you another way.
"""

print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

"""
The backslash (\) has a very special meaning when used inside strings ‒ this is called the escape character.
In other words, the backslash doesn't mean anything in itself,
but is only a kind of announcement, that the next character after the backslash has a different meaning too.
The letter "n" placed after the backslash comes from the word newline.
Both the backslash and the n form a special symbol named a newline character, which urges the console to start a new output line.
"""