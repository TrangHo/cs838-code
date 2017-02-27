from lib.constants import universityNouns
import re

# 17(T). One word University: "Harvard"
def test(str):
  return str in universityNouns.POPULAR_ONE_WORD_UNI
