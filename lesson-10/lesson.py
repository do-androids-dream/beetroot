try:
    10 / 0
except:
    print("yeah")


def exponent(line):
    exp = line.split("e")[1]
    if "-" in exp:
        exp = exp.removeprefix("-")
    elif "+" in exp:
        exp = exp.removeprefix("+")
    return exp


def is_float(line: str) -> bool:
    if "e" in line:
        exp = exponent(line)
        if not exp.isdigit():
            return False
        line = line.split("e")[0]

    line = (line.lstrip("-+").split("."))
    if len(line) == 2:
        for i in line:
            if i == "":
                i = "0"
            if not i.isdigit():
                return False
        return True
    return False

print("POSITIVE:")
print("0.25", is_float("0.25"))
print(".25", is_float(".25"))
print("+0.25", is_float("+0.25"))
print("-0.25", is_float("-0.25"))
print("+---0.25", is_float("+---0.25"))
print("0.0", is_float("0.0"))
print(".0", is_float(".0"))
print("0.0", is_float("0."))
print(1.0e+3, is_float("1.0e-3"))
print(1.e+3, is_float("1.e-3"))
print(.1e-3, is_float("0.1e-3"))
print(.1e+3, is_float("0.1e+3"))
print("\nNEGATIVE:")
print("0", is_float("0"))
print("", is_float(""))
print("abc", is_float("abc"))
print("a.b", is_float("a.b"))
print("+0.25.25", is_float("+0.25.25"))
print("+---0.a", is_float("+---0.a"))
print("-0-.2", is_float("-0-.2"))
print(("1e-3.0"), is_float("1e-3.0"))
print(".1e++3", is_float("0.1e++3"))
print(".1e+3+", is_float("0.1e+3+"))
