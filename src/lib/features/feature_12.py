from lib.constants import university_nouns
import re

# 12(T). Whether it has suffix: "'(s) ... graduate"
#   - Whether it has suffix: "'(s) ... school/center"
#   - Whether it has suffix: "'(s) ... classroom"
#   - Whether it has suffix: "'(s) ... students"
#       - …’s …school/center, …’s …graduate, …(’s) classroom
#       - Thousands of <pos>U.C. Berkeley</pos>’ low-income students
def test(str, suffix):
  nouns = '|'.join(university_nouns.NOUNS_GO_WITH_UNIVERSITIES)
  pattern = re.compile("^'(?:s)?\\s*(\\b\w\w+\\b)*(?!,)\s*(\\b\w\w+\\b)*\\b(" + nouns + ")")
  return re.search(pattern, suffix)
