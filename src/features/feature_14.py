import re

# 14(T). Whether it has suffix: "and ... University/University..."
#   - Whether it has suffix: "and ... College/College..."
#     - <University> and …
#     - … and <university>
def test(str, suffix):
  suffix = re.sub(r'\b(of|at|in|the|-|,)\b', "", suffix)
  pattern_1 = r'^and\s+(\b[A-Z]\w+\b\s+)+(University|College)((\s+\b[a-z]\w+\b\s*)|,|($))'
  pattern_2 = r'^and\s+(University|College)(\s+\b[A-Z]\w+\b)'
  return re.search(pattern_1, suffix) or re.search(pattern_2, suffix)
