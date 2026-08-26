W = {"A": 667, "B": 667, "C": 722, "D": 722, "E": 667, "F": 611, "G": 778, "H": 722, "I": 278, "J": 500, "K": 667, "L": 556, "M": 833, "N": 722, "O": 778, "P": 667, "Q": 778, "R": 722, "S": 667, "T": 611, "U": 722, "V": 667, "W": 944, "X": 667, "Y": 667, "Z": 611, "0": 556, "1": 556, "2": 556, "3": 556, "4": 556, "5": 556, "6": 556, "7": 556, "8": 556, "9": 556, " ": 278, ".": 278, ",": 278, "-": 333, "/": 278, "\"": 355, "'": 191, "(": 333, ")": 333, ":": 278, ";": 278, "x": 500, "=": 584, "+": 584, "&": 667, "%": 889, "#": 556}

def w(s, pt):
    return sum(W.get(c, 556) for c in s) / 1000.0 * pt

def wrap(text, pt, avail, indent="   "):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        pref = "" if not lines else indent
        if w(pref + trial, pt) <= avail:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return [lines[0]] + [indent + l for l in lines[1:]]
