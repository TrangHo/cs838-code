from lib.constants import constants
import re

# 16(T). Has the form: "University of <statename>"
def test(str):
  pattern = re.compile("^University of (" + "|".join(constants.STATES) + ")")
  return re.match(pattern, str) is not None
