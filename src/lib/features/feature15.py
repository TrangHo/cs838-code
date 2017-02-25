import re

# 15(T). Whether it has the form: "... colege(s) like <...> or <...>"
#   - Whether it has the form: "... universities like <...> or <...>"
#     - private colleges like <pos>Middlebury</pos> or <pos>Champlain</pos>
#     ⁃ universities like <pos>Harvard</pos>
def test(str, prefix):
  prefix = re.sub(r'\b(of|at|in|the|-|,)\b', "", prefix)
  pattern = r'\b((college(?:s)?)|university|universities)\b\s+like(?:\s+\b[A-Z]\w+\b\s+(\b[A-Z]\w+\b\s+)+or)?$'
  return re.search(pattern, prefix) is not None
