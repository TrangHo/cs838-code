import re
from lib.constants import universityNouns, prefixKeywords

POS_MARKUP = r'<pos>(\w|-|,|\.|\s)+</pos>'

NEG_PATTERN_1 = r'([A-Z][a-z]+(?=\s[A-Z])(?:\s[A-Z][a-z]+)+)'
NEG_PATTERN_2 = r'\b(at|from|in)\s([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)'
NEG_PATTERN_3 = re.compile('((\\b(\w|\d|\'|,|-|:|;)+\\b)(\s+\\b(\w|\d|\'|,|-|:|;)+\\b){2,3})\s+(?:\'(?:s)?)?(' + '|'.join(universityNouns.NOUNS_GO_WITH_UNIVERSITIES) + ')')
NEG_PATTERN_4 = re.compile('(' + '|'.join(prefixKeywords.PREFIX_KEYWORDS) + ')\s+((\\b(\w|\d|\'|,|-|:|;)+\\b)(\s+\\b(\w|\d|\'|,|-|:|;)+\\b){2,3})')

NEG_PATTERNS = [
  [NEG_PATTERN_1, 0],
  [NEG_PATTERN_2, 2],
  [NEG_PATTERN_3, 1],
  [NEG_PATTERN_4, 2]
]
