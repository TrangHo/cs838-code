import re
from lib.constants import universityNouns
# Whether it has one these prefixes: "attend(ed)"
def test(str, prefix):
    pattern = re.compile('(attend|attended)$')
    return re.search(pattern, prefix) is not None
