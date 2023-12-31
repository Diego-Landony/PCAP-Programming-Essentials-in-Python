## 2.1.12 LAB: The `print()` function and its arguments

### Scenario

Modify the first line of code in the editor, using the `sep` and `end` keywords, to match the expected output. Use the two `print()` functions in the editor.

Don't change anything in the second `print()` invocation.

### Expected output

```
Programming***Essentials***in...Python
```

code:
```python
print("Programming","Essentials","in")
print("Python")
```

---

## 2.1.13 LAB: Formatting the output

### Scenario

We strongly encourage you to play with the code we've written for you, and make some (maybe even destructive) amendments. Feel free to modify any part of the code, but there is one condition ‒ learn from your mistakes and draw your own conclusions.

Try to:

- Minimize the number of `print()` function invocations by inserting the `\n` sequence into the strings.
- Make the arrow twice as large (but keep the proportions).
- Duplicate the arrow, placing both arrows side by side. Note: a string may be multiplied by using the following trick: `"string" * 2` will produce `"stringstring"` (we'll tell you more about it soon).
- Remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error ‒ is this the place where the error really exists?
- Do the same with some of the parentheses.
- Change any of the print words into something else, differing only in case (e.g., Print) ‒ what happens now?
- Replace some of the quotes with apostrophes; watch what happens carefully.

code:
```python
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
```