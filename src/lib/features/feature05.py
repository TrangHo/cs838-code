# FEATURE 4 : START WITH COLLEGE
#
# TO CHECK IF AN EXTRACTED STRING STARTS WITH THE WORD "College" OR NOT
#     TRUE - STARTS WITH THE WORD "College"
#     FALSE - OTHERWISE
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
    if words[0] == "College" or words[-1] == "College":
        return True
    else:
        return False
