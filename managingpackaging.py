from sys import stdin

track = {}
first = True
next_total = -1
count = 0
for line in stdin:
    line = line.strip()
    if first:
        first = False
        next_total = int(line)
        continue
    if count == next_total:
        count = 0
        out = []
        out_set = set()
        while True:
            to_add = ""
            for key in track:
                if track[key].issubset(out_set) and (to_add == "" or key < to_add):
                    to_add = key
            if to_add != "":
                out.append(to_add)
                out_set.add(to_add)
                del track[to_add]
            else:
                break
        if len(out) == next_total:
            print(*out, sep = "\n")
        else:
            print("cannot be ordered")
        track = {}
        in_order = []
        next_total = int(line)
        if next_total == 0:
            break
        print()
    else:
        count += 1
        if " " in line:
            track[line[:line.index(" ")]] = set(line[line.index(" ") + 1:].split(" "))
        else:
            track[line] = set()
