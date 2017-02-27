import re
from lib.constants import universityNouns
# -Whether it has one of the prefixes: "dean of ... at"
# - Whether it has the prefix: "professor(s) (of)... at"
# - Whether it has the prefix: "professor at <university>"
# - Whether it has the prefix: "professor of <univerisity>"
def test(str, prefix):
    nouns = '|'.join(universityNouns.NOUNS_GO_WITH_UNIVERSITIES)
    # pattern = re.compile('(' + nouns + ')\\s' + '\\bat')
    pattern_1 = re.compile('('+ nouns + ')\\s' + '\\bof\\s\\b(\\b[A-Za-z][a-z]+\\s\\b)+\\bat(?:\\sthe)?')
    pattern_2 = re.compile('('+ nouns + ')\\s' + '\\bof(?:\\sthe)?')
    pattern_3 = re.compile('('+ nouns + ')\\s' + '\\bat(?:\\sthe)?')
    match = re.search(pattern_1, prefix) or re.search(pattern_2, prefix) or re.search(pattern_3, prefix)
    return match is not None
