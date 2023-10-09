#!/usr/bin/python3

#The print() function has two keyword arguments that you can use for your purposes. The first is called end.
#In the editor window you can see a very simple example how to use a keyword argument.
print("My name is", "Python.", end=" ")
print("Monty Python.")

#In order to use it, it is necessary to know some rules:
#1. a keyword argument consists of three elements: a keyword identifying the argument (end here); an equal sign (=); and a value assigned to that argument;
#2. any keyword arguments have to be put after the last positional argument (this is very important)

#We said previously that the print() function separates its outputted arguments with spaces. This behavior can be changed, too.
#The keyword argument that can do this is named sep (as in separator).
#Look at the code in the editor, and run it.
print("My", "name", "is", "Monty", "Python.", sep="-")

#The print() function now uses a dash, instead of a space, to separate the outputted arguments.
#Note: the sep argument's value may be an empty string, too. Try it for yourself.


#Both keyword arguments may be mixed in one invocation, just like here in the editor window.

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#The example doesn't make much sense, but it visibly presents the interactions between "end" and "sep".