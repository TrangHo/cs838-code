#====================================================================================================
# FEATURE 1 : CAPITALIZED FIRST LETTER
#
# TO CHECK IF ALL WORDS OF AN EXTRACTED STRING HAVE THEIR FIRST LETTERS CAPITALIZED OR NOT
#     TRUE - ALL WORDS HAVE THEIR FIRST LETTERS CAPITALIZED
#     FALSE - OTHERWISE
#
# NOTE: THIS DOES NOT CONSIDER PREPOSITION WORDS, SUCH AS "of", "at", "in", "for"
#
#====================================================================================================

def relevant(word):
    if (word == "of") or (word == "at") or (word == "in") or (word == "for"):
        return False
    else:
        return True

def preprocessing(s):
    s = s.replace(",", " ").replace("-", " ").replace(".", " ")

def test(s):
    words = s.split()
    toreturn = True
    for word in words:
        if (relevant(word)) and word[0].islower():
            toreturn = False
            break
    return toreturn
