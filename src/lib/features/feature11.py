from lib.constants import university_nouns
import re

# 11(T). Whether it has suffix: "student(s)"
#   - Whether it has suffix: "... professor"
#   - Whether it has suffix: "... campus"
#       - <pos>Hillsdale</pos> students
#       ⁃ a <pos>Yale</pos> philosophy professor, a <pos>George Washington University</pos> law professor
#       ⁃ <pos>Berkeley</pos> campus police
#       ⁃  a <pos>Harvard</pos> political scientist
def test(str, suffix):
  nouns = '|'.join(university_nouns.NOUNS_GO_WITH_UNIVERSITIES)
  pattern = re.compile("^(\\b\w\w+\\b)*(?!,)\s*(\\b\w\w+\\b)*\\b(" + nouns + ")")
  match = re.search(pattern, suffix)
  return match is not None
