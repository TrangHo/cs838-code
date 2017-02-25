import re

# 13(T). Whether it has a prefix: "... University/University... and"
#   - Whether it has a prefix: "... College/College... and"
def test(str, prefix):
  prefix = re.sub(r'\b(of|at|in|the|-|,)\b', "", prefix)
  pattern_1 = r'(\b[A-Z]\w+\b\s+)+(University|College)\s+and$'
  pattern_2 = r'((\b[a-z]\w+\b\s+(University|College))|(^(University|College)))\s+(\b[A-Z]\w+\b\s+)+and$'
  return (re.search(pattern_1, prefix) is not None) or (re.search(pattern_2, prefix) is not None)
