from lib.constants import states
import re

# 16(T). Has the form: "University of <statename>"
def test(str):
  pattern = re.compile("^University of (" + "|".join(states.STATES) + ")")
  return re.match(pattern, str)
