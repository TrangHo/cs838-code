import re
from lib.constants import prefix_keywords
# Whether it has the keywords prefix: "receive", "degree", "M.B.A.", "master"
#     - Whether it has the prefix: "received a/an (M.B.A.)/(... degree) (in ...) from"
#     - and received a law degree from the <pos>University of Pennsylvania</pos>
#     - He graduated cum laude from <pos>Middlebury College</pos> and received an M.B.A. from <pos>Stanford</pos>
#     - He graduated from <pos>Virginia Tech</pos>, and received an M.B.A. in finance from <pos>Washington University</pos> in St. Louis.
def test(str, prefix):
    nouns = '|'.join(prefix_keywords.PREFIX_KEYWORDS)
    # pattern = re.compile('(' + nouns + ')\\s' + '\\bat')
    pattern = re.compile('('+ nouns + ')')
    return re.search(pattern, prefix) is not None
