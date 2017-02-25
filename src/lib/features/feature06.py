import re
from lib.constants import universityNouns
# -Whether it has one of the prefixes: "dean of ... at"
# - Whether it has the prefix: "professor(s) (of)... at"
def test(str, prefix):
    nouns = '|'.join(universityNouns.NOUNS_GO_WITH_UNIVERSITIES)
    # pattern = re.compile('(' + nouns + ')\\s' + '\\bat')
    pattern = re.compile('('+ nouns + ')\\s' + '\\bof\\s\\b(\\b[A-Za-z][a-z]+\\s\\b)+\\bat')
    return re.search(pattern, prefix) is not None
