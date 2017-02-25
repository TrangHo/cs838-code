import re

# Whether it has suffix: ",/- a/an ... college"
#   - Whether it has suffix: ",/- a/an ... university"
#   - Whether it has suffix: ",/- the ... university"
#   - Whether it has suffix: ",/- the ... college"

#     - <pos>Hillsdale</pos>, a private college
#     - <pos>Hillsdale</pos>, a conservative college in Michigan
#     ⁃ <pos>Arizona State</pos>, the nation's largest public university
#     - ⁃ the president of <pos>Bayan Claremont</pos>, a graduate college in Claremont, Calif.
#     - .. professor/student, prefix or post fix with ‘,/-/apostrophe(s)’ . Eg John Something, a Harvard professor,
def test(str, suffix):
    #pattern = re.compile("^(\\b[a-z]+\\b)*(?!,)\\s*(a|an|the)\\s(\\b[a-z]+\\s\\b)*(university|college)")
    pattern = re.compile("^(?!,)\\s*(a|an|the)\\s(\\b[a-z]+('s)?\\s\\b)*(university|college)")
    return re.search(pattern, suffix) is not None
