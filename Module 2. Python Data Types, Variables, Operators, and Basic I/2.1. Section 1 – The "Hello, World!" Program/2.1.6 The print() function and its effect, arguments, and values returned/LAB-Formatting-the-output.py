#!/usr/bin/python3

###################
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print()
#- Minimize the number of `print()` function invocations by inserting the `\n` sequence into the strings.
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")
print()
#- Make the arrow twice as large (but keep the proportions).
print("        *        ")
print("       * *       ")
print("      *   *      ")
print("     *     *     ")
print("    *       *    ")
print("   *         *   ")
print("  *           *  ")
print(" *             * ")
print("******     ******")
print("     *     *     ")
print("     *     *     ")
print("     *     *     ")
print("     *     *     ")
print("     *     *     ")
print("     *     *     ")
print("     *******     ")
#- Duplicate the arrow, placing both arrows side by side. Note: a string may be multiplied by using the following trick: `"string" * 2` will produce `"stringstring"` (we'll tell you more about it soon).
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)
#- Remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error ‒ is this the place where the error really exists?

#SyntaxError: invalid syntax

#print(    *) 
#print("   * *")
#print("  *   *")
#print(" *     *")
#print("***   ***")
#print("  *   *")
#print("  *   *")
#print("  *****")

#- Do the same with some of the parentheses.

#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

#print"    *" 
#print("   * *")
#print("  *   *")
#print(" *     *")
#print("***   ***")
#print("  *   *")
#print("  *   *")
#print("  *****")

#- Change any of the print words into something else, differing only in case (e.g., Print) ‒ what happens now?

#Se produjo una excepción: NameError
#name 'Print' is not defined

#Print("    *")
#print("   * *")
#print("  *   *")
#print(" *     *")
#print("***   ***")
#print("  *   *")
#print("  *   *")
#print("  *****")


#- Replace some of the quotes with apostrophes; watch what happens carefully.

#also it works. 
#print('    *')
#print("   * *")
#print("  *   *")
#print(" *     *")
#print("***   ***")
#print("  *   *")
#print("  *   *")
#print("  *****")
