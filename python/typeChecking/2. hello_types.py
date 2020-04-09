""" Example 1 """
def headline(text, align=True):
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else: 
        return f" {text.title()} ".center(50, "o")

print(headline("python type checking"))
# result: 
# Python Type Checking
# --------------------

print(headline("python type checking", align=False))
# result: 
# oooooooooooooo Python Type Checking oooooooooooooo


""" Example 2 """
def headline2(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else: 
        return f" {text.title()} ".center(50, "o")

print(headline2("python type checking", align="left"))
# reulst:
# Python Type Checking
# --------------------