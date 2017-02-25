POS_MARKUP = r'<pos>(\w|-|,|\.|\s)+</pos>'

NEG_PATTERN_1 = r'([A-Z][a-z]+(?=\s[A-Z])(?:\s[A-Z][a-z]+)+)'
NEG_PATTERN_2 = r'\b(at|from|in)\s([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)'

NEG_PATTERNS = [[NEG_PATTERN_1, 0], [NEG_PATTERN_2, 2]]
