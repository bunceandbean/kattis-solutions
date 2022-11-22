#Author: Ben Lilley

from sys import stdin
#pqrst variables
vars = ["p","q","r","s","t"]

#All possible permutations of PQRST
layout = {(1, 1, 1, 0, 0), (0, 1, 0, 0, 1), (0, 0, 1, 0, 0), (1, 0, 1, 1, 0), (0, 0, 0, 0, 0), (0, 1, 1, 1, 1), (1, 1, 1, 1, 1), (1, 0, 0, 1, 0), (1, 1, 0, 0, 0), (0, 0, 1, 1, 1), (1, 0, 0, 0, 1), (0, 1, 0, 0, 0), (0, 0, 0, 1, 1), (1, 0, 1, 0, 1), (0, 1, 1, 1, 0), (0, 1, 0, 1, 1), (1, 1, 1, 1, 0), (0, 0, 1, 1, 0), (1, 1, 0, 1, 1), (0, 1, 1, 0, 1), (0, 0, 0, 1, 0), (1, 1, 1, 0, 1), (1, 0, 0, 0, 0), (1, 0, 1, 0, 0), (1, 0, 1, 1, 1), (0, 0, 1, 0, 1), (1, 0, 0, 1, 1), (0, 0, 0, 0, 1), (0, 1, 0, 1, 0), (1, 1, 0, 1, 0), (0, 1, 1, 0, 0), (1, 1, 0, 0, 1)}

for line in stdin:
    line = line.strip()
    if line == "0":
        break
    leave = False
    # For every permutation...
    for bin in layout:
        new_l = line
        # Set the new logic string to match the permutation for PQRST
        for i in range(len(vars)):
            new_l = new_l.replace(vars[i], str(bin[i]))
        #While we still have logic symbols in our new logic string (new_l), replace them with their logical equivalent 0 or 1 based on the given table
        while "K" in new_l or "A" in new_l or "N" in new_l or "C" in new_l or "E" in new_l:
            new_l = new_l.replace("N0", "1")
            new_l = new_l.replace("N1", "0")
            new_l = new_l.replace("K11", "1")
            new_l = new_l.replace("K10", "0")
            new_l = new_l.replace("K01", "0")
            new_l = new_l.replace("K00", "0")

            new_l = new_l.replace("A11", "1")
            new_l = new_l.replace("A10", "1")
            new_l = new_l.replace("A01", "1")
            new_l = new_l.replace("A00", "0")

            new_l = new_l.replace("C11", "1")
            new_l = new_l.replace("C10", "0")
            new_l = new_l.replace("C01", "1")
            new_l = new_l.replace("C00", "1")


            new_l = new_l.replace("E11", "1")
            new_l = new_l.replace("E10", "0")
            new_l = new_l.replace("E01", "0")
            new_l = new_l.replace("E00", "1")
        # If we ever end with a "0" (False), we know it cannot be a tautology. Print "not" and set leave = true to not print the tautology string
        if new_l == "0":
            print("not")
            leave = True
            break
    # If our new logic string was never 0 for every permutation, we know we have a tautology
    if not leave:
        print("tautology")
